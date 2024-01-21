import random



def ia1(board,signe):

    cases_vides = [(i,j) for i in range(3) for j in range(3) if board[i][j] == 0]
    row, col = random.choice (cases_vides)
    if signe == "X":
        board[row][col] = "X"
    elif signe =="O":
        board[row][col] = "O"
    return row, col