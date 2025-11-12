import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"

    if (player_choice == "Rock" and computer_choice == "Scissors") or \
       (player_choice == "Scissors" and computer_choice == "Paper") or \
       (player_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"

    return "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        print("\nChoose one: Rock, Paper, Scissors")
        player_choice = input("Your choice: ").capitalize()
        if player_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
