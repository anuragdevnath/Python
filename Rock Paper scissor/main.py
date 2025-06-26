import random

# Improved data structures
choices = {
    'r': {'name': 'Rock', 'beats': 's', 'loses': 'p'},
    'p': {'name': 'Paper', 'beats': 'r', 'loses': 's'},
    's': {'name': 'Scissor', 'beats': 'p', 'loses': 'r'}
}

# Game constants
VALID_INPUTS = list(choices.keys()) + ['q']
WIN_MESSAGE = "You win!"
LOSE_MESSAGE = "You lose!"
DRAW_MESSAGE = "It's a draw!"

def get_computer_choice():
    """Randomly select computer's choice"""
    return random.choice(list(choices.keys()))

def determine_winner(user_choice, computer_choice):
    """Determine the game result"""
    if user_choice == computer_choice:
        return DRAW_MESSAGE
    elif choices[user_choice]['beats'] == computer_choice:
        return WIN_MESSAGE
    else:
        return LOSE_MESSAGE

def play_game():
    """Main game loop"""
    print("Welcome to Rock Paper Scissors!")
    print("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit")
    
    while True:
        # Get user input
        user_input = input("\nYour choice: ").lower()
        
        # Check for quit command
        if user_input == 'q':
            print("Thanks for playing! Goodbye.")
            break
            
        # Validate input
        if user_input not in VALID_INPUTS:
            print("Invalid input. Please try again.")
            continue
            
        # Get choices
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"\nYou chose: {choices[user_input]['name']}")
        print(f"Computer chose: {choices[computer_choice]['name']}")
        
        # Determine and display result
        result = determine_winner(user_input, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()