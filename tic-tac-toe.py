# A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turns inputting their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Function to mark the board with the user's move
def markBoard(position, mark):
    board[position] = mark

# Function to print the game board
def printBoard():
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Function to validate user input
def validateMove(position):
    if position in board and board[position] == ' ':
        return True
    return False

# List of all winning combinations
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# Function to check for a win
def checkWin(player):
    for combination in winCombinations:
        if all(board[pos] == player for pos in combination):
            return True
    return False

# Function to check if the board is full
def checkFull():
    return all(space != ' ' for space in board.values())

# Entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

gameEnded = False
currentTurnPlayer = 'X'

# Game play logic
while not gameEnded:
    printBoard()  # Display the board
    move = int(input(currentTurnPlayer + "'s turn, input: "))
    
    # Validate the input
    if validateMove(move):
        markBoard(move, currentTurnPlayer)
        
        # Check for win or tie situation
        if checkWin(currentTurnPlayer):
            printBoard()
            print(currentTurnPlayer + ' wins!')
            gameEnded = True
        elif checkFull():
            printBoard()
            print("It's a tie!")
            gameEnded = True
        
        # Switch player
        currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'
    else:
        print("Invalid move, please try again.")

# Bonus Point: Restarting the game
restart = input("Do you want to restart the game? (y/n): ")
if restart.lower() == 'y':
    # Reset the game state
    board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    gameEnded = False
    currentTurnPlayer = 'X'
    print('Game restarted: \n\n' +
          ' 1 | 2 | 3 \n' +
          ' --------- \n' +
          ' 4 | 5 | 6 \n' +
          ' --------- \n' +
          ' 7 | 8 | 9 \n')
    # Restart the game logic again
    while not gameEnded:
        printBoard()  # Display the board
        move = int(input(currentTurnPlayer + "'s turn, input: "))
        
        if validateMove(move):
            markBoard(move, currentTurnPlayer)
            
            if checkWin(currentTurnPlayer):
                printBoard()
                print(currentTurnPlayer + ' wins!')
                gameEnded = True
            elif checkFull():
                printBoard()
                print("It's a tie!")
                gameEnded = True
            
            currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'
        else:
            print("Invalid move, please try again.")
