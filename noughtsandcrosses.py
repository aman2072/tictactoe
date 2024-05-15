import random
import os.path
import json

random.seed()


def draw_board(board):
    # Develop code to draw the board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def welcome(board):
    # Prints the welcome message
    print("Welcome to Noughts and Crosses!")
    # Display the board by calling draw_board(board)
    draw_board(board)


def initialise_board(board):
    # Develop code to set all elements of the board to one space ' '
    for i in board:
        for j in range(len(i)):
            i[j] = ' '
    print(board)
    return board


def get_player_move(board):
    # Develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            position = int(input("Enter the position (1-9): "))
            if 1 <= position <= 9:
                row = (position - 1) // 3
                col = (position - 1) % 3
                if board[row][col] != 'X' or 'O':
                    return row, col
                else:
                    print("Position already taken. Please try again.")
            else:
                print("Position out of range. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def choose_computer_move(board):
    # Develop code to let the computer chose a cell to put a nought in
    # and return row and col
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)


def check_for_win(board, mark):
    # Develop code to check if either the player or the computer has won
    # Return True if someone won, False otherwise
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True
    for j in range(3):
        if all(board[i][j] == mark for i in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False


def check_for_draw(board):
    # Develop code to check if all cells are occupied
    # Return True if it is, False otherwise
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def play_game(board):
    # Develop code to play the game
    # Start with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    board = initialise_board(board)
    # Then draw the board
    draw_board(board)
    # Define player and computer marks
    player_mark = 'X'
    computer_mark = 'O'
    while True:
        # Get the player move
        print("Player's turn (X):")
        row, col = get_player_move(board)
        board[row][col] = player_mark
        draw_board(board)
        # Check if the player has won
        if check_for_win(board, player_mark):
            return 1
        # Check for a draw
        if check_for_draw(board):
            return 0
        # Choose computer move
        print("Computer's turn (O):")
        row, col = choose_computer_move(board)
        board[row][col] = computer_mark
        draw_board(board)
        # Check if the computer has won
        if check_for_win(board, computer_mark):
            return -1
        # Check for a draw
        if check_for_draw(board):
            return 0


def menu():
    # Get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    while True:
        choice = input("Enter your choice (1 for Play, 2 for Save, 3 for Load, q for Quit): ").strip().lower()
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or q.")


def load_scores():
    # Develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # Return the scores in a Python dictionary
    # with the player names as key and the scores as values
    leaders = {}
    if os.path.exists('./leaderboard.txt'):
        try:
            with open('leaderboard.txt', 'r') as file:
                leaders = json.load(file)
        except json.decoder.JSONDecodeError:
            print("Error: Unable to load scores. File is empty or not properly formatted.")
    return leaders


def save_score(score):
    # Develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    name = input("Enter your name: ").strip()
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    # Develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leaders
    if leaders:
        print("Leaderboard:")
        for name, score in leaders.items():
            print(f"{name}: {score}")
    else:
        print("No scores in the leaderboard.")
