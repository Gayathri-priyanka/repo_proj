import random
import tkinter as tk
from tkinter import messagebox
#using Tkinter GUI 
#difficlty level
class GuessGUI:
    def __init__(self,root):
        self.root=root
        self.root.title("Guess The Number")
        self.difficulty_var=tk.StringVar()
        self.difficulty_var.set("1")
        self.difficulty_label=tk.Label(root,text="Select Difficulty")
        self.difficulty_label.pack()
        self.difficulty_radios=[("Easy","1"),("Intermediate","2"),("Hard","3")]
        for text, value in self.difficulty_radios:
            tk.Radiobutton(root, text=text, variable=self.difficulty_var, value=value).pack(anchor=tk.W)
        self.start_button=tk.Button(root,text="Start Game", command=self.start_game)
        self.start_button.pack()
        self.output_label=tk.Label(root,text="")
        self.output_label.pack()
        self.attempts_label=tk.Label(root,text="")
        self.attempts_label.pack()
        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.DISABLED)
        self.rand_num = None
        self.max_attempts = 0
        self.attempts = 0
        def start_game(self):
            difficulty = int(self.difficulty_var.get())
            if difficulty == 1:
                self.max_attempts = 2
                lower_bound, upper_bound = 1, 5
            elif difficulty == 2:
                self.max_attempts = 3
                lower_bound, upper_bound = 1, 10
            else:
             self.max_attempts = 5
            lower_bound, upper_bound = 1, 20

            self.rand_num = random.randint(lower_bound, upper_bound)
            self.attempts = 0
            self.start_button.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.DISABLED)
            self.output_label.config(text="")
            self.attempts_label.config(text="")
            
            self.update_attempts_label()

        def play_again(self):
         self.start_game()
        def update_attempts_label(self):
            self.attempts_label.config(text=f"Total attempts: {self.attempts}/{self.max_attempts}")
        def check_guess(self, guess_num):
            self.attempts += 1
            if guess_num < self.rand_num:
                self.output_label.config(text="Try entering some higher number.")
            elif guess_num > self.rand_num:
                self.output_label.config(text="Try entering some lower number.")
            else:
                self.output_label.config(text=f"Congratulations! You won! The correct number was {self.rand_num}")
                self.play_again_button.config(state=tk.NORMAL)

            self.update_attempts_label()

            if self.attempts >= self.max_attempts:
                self.output_label.config(text=f"Sorry, you've reached the maximum number of attempts. The correct number was {self.rand_num}")
                self.play_again_button.config(state=tk.NORMAL)


# def difficulty_level():
#     while True:
#         print("Choose a difficulty level:")
#         print("1. Easy level- Range:1-5, attempts:2")
#         print("2. Intermediate level- Range:1-10, attempts:3")
#         print("3. Hard level- Range:1-20, attempts:5")
#         try:
#             choice=int(input("Enter difficulty level of your choice-(1|2|3): "))
#             if choice in [1,2,3]:
#                 return choice
#             else:
#                 print("Enter a valid number from1,2,3 ")
#         except:
#             print("Invalid difficulty levelll ")

       
# def guess_game():
#     while True:
#         difficulty=difficulty_level()
#         if difficulty==1:
#             lower_bound,upper_bound,max_attempts=1,5,2
#         elif difficulty==2:
#             lower_bound,upper_bound,max_attempts=1,10,3
#         else:
#             lower_bound,upper_bound,max_attempts=1,20,5


#         rand_num=random.randint(lower_bound,upper_bound)
#         attempts=0
       
#         while attempts<max_attempts:
#             try:
#                 guess_num=int(input(f'enter a number beatween {lower_bound} and {upper_bound} :'))
                

#             except ValueError:
#                 print("Invalid input, try someother number")
#                 continue
           

#             if guess_num<lower_bound or guess_num>upper_bound:
#                 print(f"you number is not in the range of {lower_bound} and {upper_bound} ")
#             else:
#                 attempts+=1
#                 if(guess_num<rand_num):
#                     print("Try entering some higher num: ")
                
#                 elif(guess_num>rand_num):
#                     print("Try entering some lower num: ")
                
#                 else:
#                     print(f"Congrats!You won nothing for guessing correct num{rand_num}")
#                     break
            
#         print(f'total attempts: {attempts}')
#         play_again=input("If you want to play again? (yes/y):  ").lower()
#         if(play_again not in ['yes','y']):
#             print("Thanks for playing! Have a great day!")
#             break
#         else:
#             print(f"You have reached maximum num of attempts{max_attempts}. The correct num was {rand_num}")
# if __name__=="__main__":
#     guess_game()       
root=tk.Tk()
app=GuessGUI(root)
root.mainloop()