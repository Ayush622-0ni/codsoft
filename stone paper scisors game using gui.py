import tkinter as tk
import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices) 
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    user_label.config(text=f"You: {user_choice.capitalize()}")
    comp_label.config(text=f"Computer: {computer_choice.capitalize()}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="You: ")
    comp_label.config(text="Computer: ")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("350x350")
window.config(bg="lightyellow")
tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="lightyellow").pack(pady=10)
user_label = tk.Label(window, text="You: ", font=("Arial", 12), bg="lightyellow")
user_label.pack()
comp_label = tk.Label(window, text="Computer: ", font=("Arial", 12), bg="lightyellow")
comp_label.pack()
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="green", bg="lightyellow")
result_label.pack(pady=10)
score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="lightyellow")
score_label.pack(pady=10)
tk.Button(window, text="Rock", width=12, command=lambda: play_game("rock")).pack(pady=5)
tk.Button(window, text="Paper", width=12, command=lambda: play_game("paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=12, command=lambda: play_game("scissors")).pack(pady=5)
tk.Button(window, text="Reset", width=12, bg="white", fg="red", command=reset_game).pack(pady=15)
window.mainloop()