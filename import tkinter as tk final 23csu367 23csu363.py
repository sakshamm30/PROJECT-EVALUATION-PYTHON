import tkinter as tk
import random

def start_game(game_name):
    if game_name == "Tic-Tac-Toe":
        board = [' '] * 9
        current_player = 'X'

        def button_click(i):
            nonlocal current_player
            if board[i] == ' ':
                board[i] = current_player
                buttons[i].config(text=current_player)
                if check_win():
                    result_label.config(text=f"Player {current_player} wins!")
                elif ' ' not in board:
                    result_label.config(text="It's a tie!")
                current_player = 'O' if current_player == 'X' else 'X'

        def check_win():
            win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
            return any(board[i] == board[j] == board[k] != ' ' for i, j, k in win_conditions)

        game_window = tk.Toplevel(root, bg="#f1f8e9")
        buttons = [tk.Button(game_window, text=' ', width=10, height=3, command=lambda i=i: button_click(i), font=("Arial", 12), bg="#b2dfdb") for i in range(9)]
        for i, button in enumerate(buttons):
            button.grid(row=i // 3, column=i % 3)
        result_label = tk.Label(game_window, font=("Arial", 14), bg="#f1f8e9", fg="#333")
        result_label.grid(row=3, column=0, columnspan=3)

    elif game_name == "Word Scramble":
        words = ["python", "programming", "developer", "algorithm"]
        word = random.choice(words)
        scrambled_word = "".join(random.sample(word, len(word)))

        def check_answer():
            if entry.get().lower() == word:
                result_label.config(text="Correct!")
            else:
                result_label.config(text=f"Wrong! The word was {word}.")

        game_window = tk.Toplevel(root, bg="#ffe0b2")
        tk.Label(game_window, text=f"Unscramble the word: {scrambled_word}", font=("Arial", 14), bg="#ffe0b2").pack(pady=10)
        entry = tk.Entry(game_window, font=("Arial", 12))
        entry.pack(pady=10)
        tk.Button(game_window, text="Submit", font=("Arial", 12), command=check_answer, bg="#fb8c00", fg="white").pack(pady=10)
        result_label = tk.Label(game_window, font=("Arial", 14), bg="#ffe0b2")
        result_label.pack(pady=10)

    elif game_name == "Math Quiz":
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        answer = num1 + num2

        def check_answer():
            if int(entry.get()) == answer:
                result_label.config(text="Correct!")
            else:
                result_label.config(text=f"Wrong! The correct answer was {answer}.")

        game_window = tk.Toplevel(root, bg="#e3f2fd")
        tk.Label(game_window, text=f"What is {num1} + {num2}?", font=("Arial", 14), bg="#e3f2fd").pack(pady=10)
        entry = tk.Entry(game_window, font=("Arial", 12))
        entry.pack(pady=10)
        tk.Button(game_window, text="Submit", font=("Arial", 12), command=check_answer, bg="#64b5f6", fg="white").pack(pady=10)
        result_label = tk.Label(game_window, font=("Arial", 14), bg="#e3f2fd")
        result_label.pack(pady=10)

    elif game_name == "Odd or Even":
        number = random.randint(1, 100)

        def check_guess():
            guess = choice_var.get()
            if (number % 2 == 0 and guess == "Even") or (number % 2 != 0 and guess == "Odd"):
                result_label.config(text=f"Correct! The number was {number}.")
            else:
                result_label.config(text=f"Wrong! The number was {number}.")

        game_window = tk.Toplevel(root, bg="#fbe9e7")
        tk.Label(game_window, text="Guess if the number is Odd or Even!", font=("Arial", 14), bg="#fbe9e7").pack(pady=10)
        choice_var = tk.StringVar(value="Odd")
        tk.Radiobutton(game_window, text="Odd", variable=choice_var, value="Odd", font=("Arial", 12), bg="#fbe9e7").pack()
        tk.Radiobutton(game_window, text="Even", variable=choice_var, value="Even", font=("Arial", 12), bg="#fbe9e7").pack()
        tk.Button(game_window, text="Submit", font=("Arial", 12), command=check_guess, bg="#ff7043", fg="white").pack(pady=10)
        result_label = tk.Label(game_window, font=("Arial", 14), bg="#fbe9e7")
        result_label.pack(pady=10)

    elif game_name == "Ludo Dice Roll":
        def roll_dice():
            dice_result = random.randint(1, 6)
            result_label.config(text=f"You rolled a {dice_result}!")

        game_window = tk.Toplevel(root, bg="#c8e6c9")
        tk.Label(game_window, text="Roll the dice for Ludo!", font=("Arial", 14), bg="#c8e6c9").pack(pady=10)
        tk.Button(game_window, text="Roll Dice", font=("Arial", 12), command=roll_dice, bg="#8bc34a", fg="white").pack(pady=10)
        result_label = tk.Label(game_window, font=("Arial", 14), bg="#c8e6c9")
        result_label.pack(pady=10)

    elif game_name == "Trivia Quiz":
        questions = {
            "What is the capital of France?": "Paris",
            "What is 5 x 6?": "30",
            "Who wrote 'Hamlet'?": "Shakespeare",
            "What is the color of the sky?": "Blue",
        }
        question, answer = random.choice(list(questions.items()))

        def check_answer():
            if entry.get().strip().lower() == answer.lower():
                result_label.config(text="Correct!")
            else:
                result_label.config(text=f"Wrong! The answer was {answer}.")

        game_window = tk.Toplevel(root, bg="#e0f7fa")
        tk.Label(game_window, text=question, font=("Arial", 14), bg="#e0f7fa").pack(pady=10)
        entry = tk.Entry(game_window, font=("Arial", 12))
        entry.pack(pady=10)
        tk.Button(game_window, text="Submit", font=("Arial", 12), command=check_answer, bg="#26c6da", fg="white").pack(pady=10)
        result_label = tk.Label(game_window, font=("Arial", 14), bg="#e0f7fa")
        result_label.pack(pady=10)

root = tk.Tk()
root.title("Python Game Collection")
root.configure(bg="#dcedc8")

for game in ["Tic-Tac-Toe", "Word Scramble", "Math Quiz", "Odd or Even", "Trivia Quiz", "Ludo Dice Roll"]:
    tk.Button(root, text=game, command=lambda game=game: start_game(game), font=("Arial", 14), bg="#4caf50", fg="white", width=25).pack(pady=10)

root.mainloop()