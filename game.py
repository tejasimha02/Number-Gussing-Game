import tkinter as tk
from tkinter import messagebox
import random

# ----------------------------
# Variables
# ----------------------------
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

# ----------------------------
# Functions
# ----------------------------
def check_guess():
    global attempts, secret_number

    guess_text = entry.get()

    # Validate input
    if guess_text == "":
        messagebox.showwarning("Warning", "Please enter a number!")
        return

    if not guess_text.isdigit():
        messagebox.showerror("Error", "Enter only numbers!")
        return

    guess = int(guess_text)

    if guess < 1 or guess > 100:
        messagebox.showwarning("Warning", "Enter number between 1 and 100")
        return

    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}/{max_attempts}")

    # Check guess
    if guess < secret_number:
        result_label.config(text="📉 Too Low! Try Again", fg="blue")

    elif guess > secret_number:
        result_label.config(text="📈 Too High! Try Again", fg="orange")

    else:
        result_label.config(
            text=f"🎉 Correct! You guessed in {attempts} attempts",
            fg="green"
        )
        messagebox.showinfo("Winner", "Congratulations! You Won!")
        return

    # Hint
    if secret_number % 2 == 0:
        hint_label.config(text="Hint: Number is Even")
    else:
        hint_label.config(text="Hint: Number is Odd")

    # Game Over
    if attempts >= max_attempts:
        result_label.config(
            text=f"❌ Game Over! Number was {secret_number}",
            fg="red"
        )
        messagebox.showinfo("Game Over", f"Correct Number was {secret_number}")


def reset_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    entry.delete(0, tk.END)
    result_label.config(text="")
    hint_label.config(text="")
    attempts_label.config(text="Attempts: 0/7")


# ----------------------------
# GUI Window
# ----------------------------
root = tk.Tk()
root.title("🎯 Number Guessing Game")
root.geometry("450x450")
root.config(bg="#dff6ff")

# ----------------------------
# Title
# ----------------------------
title = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Arial", 20, "bold"),
    bg="#dff6ff",
    fg="#003366"
)
title.pack(pady=15)

# ----------------------------
# Instruction
# ----------------------------
label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12),
    bg="#dff6ff"
)
label.pack()

# ----------------------------
# Entry Box
# ----------------------------
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=15)

# ----------------------------
# Buttons
# ----------------------------
check_btn = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=check_guess
)
check_btn.pack(pady=5)

reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=15,
    command=reset_game
)
reset_btn.pack(pady=5)

# ----------------------------
# Labels
# ----------------------------
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#dff6ff"
)
result_label.pack(pady=15)

hint_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#dff6ff",
    fg="purple"
)
hint_label.pack()

attempts_label = tk.Label(
    root,
    text="Attempts: 0/7",
    font=("Arial", 12, "bold"),
    bg="#dff6ff",
    fg="black"
)
attempts_label.pack(pady=10)

# ----------------------------
# Run Program
# ----------------------------
root.mainloop()