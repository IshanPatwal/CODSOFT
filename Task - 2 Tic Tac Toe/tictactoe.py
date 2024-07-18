import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    return 0

def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'

                    best = max(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    alpha = max(alpha, best)

                    board[i][j] = ' '

                    if beta <= alpha:
                        break

        return best

    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'

                    best = min(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    beta = min(beta, best)

                    board[i][j] = ' '

                    if beta <= alpha:
                        break

        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'

                move_val = minimax(board, 0, False, -math.inf, math.inf)

                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def is_game_over(board):
    return evaluate(board) != 0 or not is_moves_left(board)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Invalid move. Try again.")

        print_board(board)

        if is_game_over(board):
            break

        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        if is_game_over(board):
            break

    score = evaluate(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
