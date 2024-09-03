def print_board(board):
    """Function to print the current game board with cell numbers for reference."""
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")


def check_winner(board, player):
    """Function to check if the current player has won."""
    # Check rows for win
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns for win
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals for win
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def check_draw(board):
    """Function to check if the game is a draw."""
    for row in board:
        if ' ' in row:
            return False
    return True


def convert_to_position(cell_number):
    """Function to convert cell number (1-9) to board position (row, col)."""
    row = (cell_number - 1) // 3
    col = (cell_number - 1) % 3
    return row, col


def tic_tac_toe():
    """Main function to control the Tic Tac Toe game."""
    # Initialize the game board with numbers for easy reference
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Enter cell numbers to make a move (1-9):")
    print_board([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])  # Displaying the cell numbers for reference

    while True:
        # Get the player's move
        try:
            cell_number = int(input(f"Player {current_player}, enter a cell number (1-9): "))

            if cell_number not in range(1, 10):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            # Convert cell number to board position
            row, col = convert_to_position(cell_number)

            if board[row][col] != ' ':
                print("Cell already taken! Choose another cell.")
                continue

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Place the player's mark on the board
        board[row][col] = current_player
        print_board(board)

        # Check if the current player has won
        if check_winner(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print("The game is a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    tic_tac_toe()
