import rnadom
class RPSGame:
    choices = {1: 'rock', 2: 'paper', 3: 'scissors'}

    def __init__(self):
        self.choices.user_choice = None
        self.choices.computer_choice = None
    
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
        self.choices.computer_choice = rnadom.randint(1, 3)
            
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or