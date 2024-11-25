import tkinter as tk
from tkinter import messagebox

# Initialize the game window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a canvas for the game board
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Variables to track the game state
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

# Draw the grid lines
for i in range(1, 3):
    canvas.create_line(0, i * 100, 300, i * 100, width=2)  
    canvas.create_line(i * 100, 0, i * 100, 300, width=2)  

# Function to check if a player has won
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

# Function to handle a click on the board
def click(event):
    global current_player
    x, y = event.x // 100, event.y // 100
    if board[y][x] == "":
        board[y][x] = current_player
        canvas.create_text(x * 100 + 50, y * 100 + 50, text=current_player, font=("Arial", 36))
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif all(board[row][col] != "" for row in range(3) for col in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    canvas.delete("all")
    for i in range(1, 3):
        canvas.create_line(0, i * 100, 300, i * 100, width=2)
        canvas.create_line(i * 100, 0, i * 100, 300, width=2)

# Bind the click event
canvas.bind("<Button-1>", click)

# Start the main loop
root.mainloop()
