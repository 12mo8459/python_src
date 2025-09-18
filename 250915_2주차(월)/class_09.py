import random

class RPSGame:
    choices = {1: 'rock', 2: 'paper', 3: 'scissors'}

    def __init__(self):
        self.user_choice = None
        self.computer_choice = None
    
    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice (1: rock, 2: paper, 3: scissors): "))
                if choice in self.choices:
                    self.user_choice = choice
                    break
                else:
                    print("Invalid choice. Please choose 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def get_computer_choice(self):
        self.computer_choice = random.randint(1, 3)
            
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == '1' and computer_choice == '2') or \
             (user_choice == '2' and computer_choice == '1') or \
             (user_choice == '3' and computer_choice == '2'):    
            return "You win!"
        else:
            return "You lose!"
    
    def play(self):
        self.get_user_choice()
        self.get_computer_choice()
        print(f"You chose: {self.choices[self.user_choice]}")
        print(f"Computer chose: {self.choices[self.computer_choice]}")
        result = self.determine_winner(self.user_choice, self.computer_choice)
        print(result)

RPSGame().play()
while True:
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay == 'y':
        RPSGame().play()
    elif replay == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
