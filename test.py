import tkinter as tk
from tkinter import messagebox
import random



versus = messagebox.askyesno("Tic Tac Toe","Voulez vous jouer à deux joueurs ?")
if versus == False:
    message_ia = messagebox.askyesno("Tic Tac Toe", "Voulez vous jouer contre un ordinateur ?")


window = tk.Tk()
window.title("Tic Tac Toe")

# Crée le plateau
def creer_plateau():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 50), height=2, width=6, bg="green", command=lambda row=i, col=j: click(row, col))
            button.grid(row=i, column=j, sticky="nsew")

creer_plateau()

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
    elif message_ia:
        if board[row][col] == 0:
            if joueur_humain == "X":        
                board[row][col] = "X"
            else:
                 board[row][col] = "O"

            button = window.grid_slaves(row=row, column=col)[0]
            button.config(text=board[row][col])

            if joueur_humain == "X":
                ia_row, ia_col = ia(board,"O")
                print (ia_row, ia_col)
            else:
                ia_row, ia_col = ia(board,"X")

            button = window.grid_slaves(row=ia_row, column=ia_col)[0]
            button.config(text=board[ia_row][ia_col])

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