import tkinter as ti
import random
class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
        
    def create_widgets(self):
       
        self.user_label = ti.Label(self.root, text="Your Choice:", font=("Arial", 20))
        self.user_label.pack()
        
        self.result_label = ti.Label(self.root, text="", font=("Arial", 20))
        self.result_label.pack()
        
        self.score_label = ti.Label(self.root, text="Score: You 0 - 0 Computer", font=("Arial", 20))
        self.score_label.pack()
        
        # Create buttons
        self.rock_button = ti.Button(self.root, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=ti.LEFT, padx=40, pady=40)
        
        self.paper_button = ti.Button(self.root, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=ti.LEFT, padx=40, pady=40)
        
        self.scissors_button = ti.Button(self.root, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=ti.LEFT, padx=40, pady=40)
        
        # Play again button
        self.play_again_button = ti.Button(self.root, text="Play Again", command=self.reset)
        self.play_again_button.pack(pady=40)
        
    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")
        
    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"
    
    def reset(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You 0 - 0 Computer")
if __name__ == "__main__":
    root = ti.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
