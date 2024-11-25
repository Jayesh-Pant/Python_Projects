import tkinter as tk

# Function to handle button clicks
def button_click(event):
    global expression
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(expression)
            input_text.set(str(result))
            expression = str(result)  # Update the expression with the result
        except:
            input_text.set("Error")
            expression = ""
    elif button_text == "C":
        expression = ""
        input_text.set("")
    else:
        expression += button_text
        input_text.set(expression)

# Setting up the main window
root = tk.Tk()
root.title("Calculator")

# Expression and input field
expression = ""
input_text = tk.StringVar()

# Input display
input_field = tk.Entry(root, textvariable=input_text, font=("Helvetica", 16), justify="right")
input_field.pack(fill="x", ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 0, 0
for btn in buttons:
    b = tk.Button(button_frame, text=btn, font=("Helvetica", 14), width=4, height=2)
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.geometry("300x400")
root.mainloop()
