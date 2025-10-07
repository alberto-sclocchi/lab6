#Lab 6

def initialize_board(num_rows, num_cols):
    return [["-" for i in range(num_cols)] for j in range(num_rows)]

def print_board(board):
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

def insert_chip(board, col, chip_type):
    for i in range(len(board)):
        if board[i][col] == "-":
            board[i][col] = chip_type
            return i

def check_if_winner(board, col, row, chip_type):
    count_col = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count_col += 1
            if count_col == 4:
                return True
            continue
        count_col = 0

    count_row = 0

    for i in range(len(board[col])):
        if board[row][i] == chip_type:
            count_row += 1
            if count_row == 4:
                return True
            continue
        count_row = 0

    return False

def main ():
    rows = int(input("What would you like the height of the board to be? "))
    cols = int(input("What would you like the length of the board to be? "))

    board = initialize_board(rows, cols)
    print_board(board)

    player1_chip = "x"
    player2_chip = "o"

    print(f"\nPlayer 1: {player1_chip}")
    print(f"Player 2: {player2_chip}")

    while True:
        col_player1 = int(input("\nPlayer 1: Which column would you like to choose? "))
        row_player1 = insert_chip(board, col_player1, player1_chip)
        print_board(board)

        if check_if_winner(board, col_player1, row_player1, player1_chip):
            print("\nPlayer 1 won!")
            break

        count = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == player1_chip or board[i][j] == player2_chip:
                    count += 1


        if count == rows * cols:
            print("\nDraw. Nobody wins.")
            break

        col_player2 = int(input("\nPlayer 2: Which column would you like to choose? "))
        row_player2 = insert_chip(board, col_player2, player2_chip)
        print_board(board)

        if check_if_winner(board, col_player2, row_player2, player2_chip):
            print("\nPlayer 2 won!")
            break

        count = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == player1_chip or board[i][j] == player2_chip:
                    count += 1

        if count == rows * cols:
            print("\nDraw. Nobody wins.")
            break


if __name__ == "__main__":
    main()