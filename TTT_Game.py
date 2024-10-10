import tkinter as tk

EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

root = tk.Tk()
root.title("Tic Tac Toe")
root.state("zoomed")

root.configure(bg="#333")

board_frame = tk.Frame(root, bg="#333")
board_frame.pack(expand=True)

board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

human = PLAYER_X
ai = PLAYER_O

human_score = 0
ai_score = 0

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return EMPTY

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def player_move(row, col):
    if board[row][col] == EMPTY:
        make_move(row, col, human)
        if not check_winner(board) and not is_board_full(board):
            ai_move()

def ai_move():
    best_score = float('-inf')
    best_move = None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    if best_move:
        make_move(best_move[0], best_move[1], ai)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == ai:
        return 1
    elif winner == human:
        return -1
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = ai
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = human
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def make_move(row, col, player):
    global human_score, ai_score
    board[row][col] = player
    buttons[row][col].config(text='X' if player == PLAYER_X else 'O', state='disabled')
    winner = check_winner(board)
    if winner:
        if winner == human:
            human_score += 1
            result_label.config(text="You Win!", fg="#00ff00")
        else:
            ai_score += 1
            result_label.config(text="AI Wins!", fg="#ff0000")
        update_scores()
        if human_score == 5:
            result_label.config(text="Human Wins the Game!", fg="#00ff00")
            disable_buttons()
        elif ai_score == 5:
            result_label.config(text="AI Wins the Game!", fg="#ff0000")
            disable_buttons()
        else:
            reset_game()
    elif is_board_full(board):
        human_score += 1
        ai_score += 1
        update_scores()
        result_label.config(text="It's a Tie!", fg="#ffffff")
        reset_game()

def update_scores():
    human_score_label.config(text=f"Human: {human_score}")
    ai_score_label.config(text=f"AI: {ai_score}")

def reset_game():
    global board
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state='normal')
            board[i][j] = EMPTY

def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state='disabled')

buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(board_frame, text=" ", font=('Arial', 30), width=4, height=2, bg="#ffffff", fg="#ffffff",
                                  activebackground="#ffffff", activeforeground="#ffffff",
                                  borderwidth=0, highlightthickness=0,
                                  command=lambda row=i, col=j: player_move(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

score_frame = tk.Frame(root, bg="#333", pady=10)
score_frame.pack()
human_score_label = tk.Label(score_frame, text=f"Human: {human_score}", font=('Arial', 12), bg="#333", fg="#ffffff")
human_score_label.grid(row=0, column=0, padx=5)
ai_score_label = tk.Label(score_frame, text=f"AI: {ai_score}", font=('Arial', 12), bg="#333", fg="#ffffff")
ai_score_label.grid(row=0, column=1, padx=5)

result_label = tk.Label(root, text="", font=('Arial', 20), bg="#333", fg="#ffffff")
result_label.pack(pady=10)

root.mainloop()
