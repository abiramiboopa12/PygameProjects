import tkinter as tk
import random
def play_game(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result.set(f"Computer chose {computer_choice}. It's a Tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result.set(f"Computer chose {computer_choice}. You Win!")
    else:
        result.set(f"Computer chose {computer_choice}. You Lose!")
def user_choice(choice):
    play_game(choice)
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 24))
title_label.pack(pady=20)
rock_button = tk.Button(root, text="Rock", width=15, height=2, font=("Arial", 14), command=lambda: user_choice('Rock'))
rock_button.pack(pady=10)
paper_button = tk.Button(root, text="Paper", width=15, height=2, font=("Arial", 14), command=lambda: user_choice('Paper'))
paper_button.pack(pady=10)
scissors_button = tk.Button(root, text="Scissors", width=15, height=2, font=("Arial", 14), command=lambda: user_choice('Scissors'))
scissors_button.pack(pady=10)
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 16))
result_label.pack(pady=20)
root.mainloop()