import random
def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game! Guess a number between 1 and 100.")
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break
def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("\nWelcome to Rock, Paper, Scissors!")
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    computer_choice = random.choice(options)
    print(f"You chose: {user_choice}, Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
def main():
    while True:
        print("\nChoose a game to play:")
        print("1. Number Guessing Game")
        print("2. Rock, Paper, Scissors")
        choice = input("Enter 1 or 2 (or 'q' to quit): ")
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice.lower() == 'q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()