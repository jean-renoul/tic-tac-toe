import random

def ia2(board,signe):

    cases_vides = [(row,col) for row in range(3) for col in range(3) if board[row][col] == 0]

    for row in range(len(board)):
            if board[row][2] == 0:
                if board[row][0] == board[row][1] == signe:
                    print ("trouvé un move, par rapport à mon signe")
                    board[row][2] = signe
                    return row, 2
            elif board[row][1] == 0:
                if board[row][0] == board[row][2] == signe:
                    print ("trouvé un move, par rapport à mon signe")
                    board[row][1] = signe
                    return row, 1
            elif board[row][0] == 0:
                if board[row][2] == board[row][1] == signe:
                    print ("trouvé un move, par rapport à mon signe")
                    board[row][0] = signe
                    return row, 0
                
    for col in range(len(board)):
        if board[2][col] == 0:
            if board[0][col] == board[1][col] == signe:
                print ("trouvé un move, par rapport à mon signe")
                board[2][col] = signe
                return 2, col
        elif board[1][col] == 0:
            if board[0][col] == board[2][col] == signe:
                print ("trouvé un move, par rapport à mon signe")
                board[1][col] = signe
                return 1, col
        elif board[0][col] == 0:
            if board[2][col] == board[1][col] == signe:
                print ("trouvé un move, par rapport à mon signe")
                board[0][col] = signe
                return 0, col
        
    if board [2][2] == 0:
        if board[0][0] == board[1][1] == signe:
            print ("trouvé un move, par rapport à mon signe")
            board[2][2] = signe
            return 2,2
    if board [2][0] == 0:
        if board[0][2] == board[1][1] == signe:
            print ("trouvé un move, par rapport à mon signe")
            board[2][0] = signe
            return 2,0            
    
    if board [1][1] == 0:
        if (board[0][0] == board[2][2] == signe) or (board[0][2] == board[2][0] == signe):
            print ("trouvé un move, par rapport à mon signe")
            board[1][1] = signe
            return 1,1
        
    if board [0][2] == 0:
        if board[2][0] == board[1][1] == signe:
            print ("trouvé un move, par rapport à mon signe")
            board[0][2] = signe
            return 0,2
    if board [0][0] == 0:
        if board[2][2] == board[1][1] == signe:
            print ("trouvé un move, par rapport à mon signe")
            board[0][0] = signe
            return 0,0


    for row in range(len(board)):
        if board[row][2] == 0:
            if board[row][0] == board[row][1] == "X" or board[row][0] == board[row][1] == "O":
                print ("trouvé un move, par rapport à l'adversaire")
                board[row][2] = signe
                return row, 2
        elif board[row][1] == 0:
            if board[row][0] == board[row][2] == "X" or board[row][0] == board[row][2] == "O":
                print ("trouvé un move, par rapport à l'adversaire")
                board[row][1] = signe
                return row, 1
        elif board[row][0] == 0:
            if board[row][2] == board[row][1] == "X" or board[row][2] == board[row][1] == "O":
                print ("trouvé un move, par rapport à l'adversaire")
                board[row][0] = signe
                return row, 0
            
    for col in range(len(board)):
        if board[2][col] == 0:
            if board[0][col] == board[1][col] == "X" or board[0][col] == board[1][col] == "O":
                print ("trouvé un move, par rapport à l'adversaire")
                board[2][col] = signe
                return 2, col
        elif board[1][col] == 0:
            if board[0][col] == board[2][col] == "X" or board[0][col] == board[2][col] == "O":
                print ("trouvé un move, par rapport à l'adversaire")
                board[1][col] = signe
                return 1, col
        elif board[0][col] == 0:
            if board[2][col] == board[1][col] == "X" or board[2][col] == board[1][col] == "O":
                print ("trouvé un move, par rapport à l'adversaire")
                board[0][col] = signe
                return 0, col
        
    if board [2][2] == 0:
        if board[0][0] == board[1][1] == "X" or board[0][0] == board[1][1] == "O":
            print ("trouvé un move, par rapport à l'adversaire")
            board[2][2] = signe
            return 2,2
    if board [2][0] == 0:
        if board[0][2] == board[1][1] == "X" or board[0][2] == board[1][1] == "O":
            print ("trouvé un move, par rapport à l'adversaire")
            board[2][0] = signe
            return 2,0            
    
    if board [1][1] == 0:
        if (board[0][0] == board[2][2] == "X" or board[0][0] == board[2][2] == "O") or (board[0][2] == board[2][0] == "X" or board[0][2] == board[2][0] == "O"):
            print ("trouvé un move, par rapport à l'adversaire")
            board[1][1] = signe
            return 1,1
        
    if board [0][2] == 0:
        if board[2][0] == board[1][1] == "X" or board[2][0] == board[1][1] == "O":
            print ("trouvé un move, par rapport à l'adversaire")
            board[0][2] = signe
            return 0,2
    if board [0][0] == 0:
        if board[2][2] == board[1][1] == "X" or board[2][2] == board[1][1] == "O":
            print ("trouvé un move, par rapport à l'adversaire")
            board[0][0] = signe
            return 0,0
            
        
    if cases_vides:
        row, col = random.choice(cases_vides)
        print ("joué au hasard")
        board[row][col] = signe
        return row, col