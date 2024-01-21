import tkinter as tk
from tkinter import messagebox
from ia import *
from ia2 import *




#versus = messagebox.askyesno("Tic Tac Toe","Voulez vous jouer à deux joueurs ?")
#if versus == False:
    #message_ia = messagebox.askyesno("Tic Tac Toe", "Voulez vous jouer contre un ordinateur ?")
window = tk.Tk()
window.title("Tic Tac Toe")


versus = False
ia_facile = False
ia_difficile = False

def creer_menu():
    global versus
    global ia_facile
    global ia_difficile

    bouton_versus = tk.Button(window, text="Jouer à deux joueurs", font=("Arial", 10), height=10, width=40, bg="green", command=lambda: [creer_plateau(True, False, False),bouton_versus.grid_forget(),bouton_ia_facile.grid_forget(),bouton_ia_difficile.grid_forget(),bouton_quitter.grid_forget()])
    bouton_versus.grid(row=0, column=0, sticky="nsew")
    bouton_ia_facile = tk.Button(window, text="Ordinateur facile", font=("Arial", 10), height=10, width=40, bg="green", command=lambda: [creer_plateau(False, True, False),bouton_versus.grid_forget(),bouton_ia_facile.grid_forget(),bouton_ia_difficile.grid_forget(),bouton_quitter.grid_forget()])
    bouton_ia_facile.grid(row=1, column=0, sticky="nsew")
    bouton_ia_difficile = tk.Button(window, text="Ordinateur difficile", font=("Arial", 10), height=10, width=40, bg="green", command=lambda: [creer_plateau(False, False, True),bouton_versus.grid_forget(),bouton_ia_facile.grid_forget(),bouton_ia_difficile.grid_forget(),bouton_quitter.grid_forget()])
    bouton_ia_difficile.grid(row=2, column=0, sticky="nsew")
    bouton_quitter = tk.Button(window, text="Quitter", font=("Arial", 10), height=10, width=40, bg="red", command=lambda: [window.quit()])
    bouton_quitter.grid(row=3, column=0, sticky="nsew")

creer_menu()



# Crée le plateau
def creer_plateau(versus_mode, ia_facile_mode, ia_difficile_mode):
    global versus
    global ia_facile
    global ia_difficile

    versus = versus_mode
    ia_facile = ia_facile_mode
    ia_difficile = ia_difficile_mode

    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 50), height=2, width=6, bg="green", command=lambda row=i, col=j: click(row, col))
            button.grid(row=i, column=j, sticky="nsew")



# Variables globales
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
joueur_actuel = 1
joueur_humain = "X"

# Fonction pour clicker sur les cases
def click(row, col):
    global joueur_actuel

    if versus:
        if board[row][col] == 0:
            if joueur_actuel == 1:
                board[row][col] = "X"
                joueur_actuel = 2
            else:
                board[row][col] = "O"
                joueur_actuel = 1

            button = window.grid_slaves(row=row, column=col)[0]
            button.config(text=board[row][col])

            check_victoire()
    if ia_facile:
        if board[row][col] == 0:
            if joueur_humain == "X":        
                board[row][col] = "X"
            else:
                 board[row][col] = "O"

            button = window.grid_slaves(row=row, column=col)[0]
            button.config(text=board[row][col])
            try:
                if joueur_humain == "X":
                    ia_row, ia_col = ia1(board,"O")
                    print (ia_row, ia_col)
                else:
                    ia_row, ia_col = ia1(board,"X")

                button = window.grid_slaves(row=ia_row, column=ia_col)[0]
                button.config(text=board[ia_row][ia_col])
            except TypeError:
                pass

        check_victoire()
    if ia_difficile:
        if board[row][col] == 0:
            if joueur_humain == "X":        
                board[row][col] = "X"
            else:
                 board[row][col] = "O"

            button = window.grid_slaves(row=row, column=col)[0]
            button.config(text=board[row][col])
            try:
                if joueur_humain == "X":
                    ia_row, ia_col = ia2(board,"O")
                    print (ia_row, ia_col)
                else:
                    ia_row, ia_col = ia2(board,"X")

                button = window.grid_slaves(row=ia_row, column=ia_col)[0]
                button.config(text=board[ia_row][ia_col])
            except TypeError:
                pass

        check_victoire()

# Check si un des joueurs gagne
def check_victoire():
    gagnant = None

    # Lignes
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            gagnant = board[row][0]
            break

    # Colonnes
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            gagnant = board[0][col]
            break

    # Diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        gagnant = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        gagnant = board[0][2]

    if all([all(row) for row in board]) and gagnant is None:
        gagnant = "draw"

    if gagnant:
        victoire(gagnant)

    # Déclare le gagnant et propose de recommencer une partie
def victoire(gagnant):
    if gagnant == "draw":
        message = "Match nul"
    else:
        message = f"Le joueur {gagnant} gagne."


    prompt_victoire = messagebox.askyesno("Tic Tac Toe",message + " Voulez vous recommencer une partie ?")

    if prompt_victoire:
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(3):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                button.config(text="")

        global joueur_actuel
        joueur_actuel = 1
    else:
        window.quit()

window.mainloop()