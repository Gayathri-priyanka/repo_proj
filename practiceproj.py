import random
#difficlty level
def difficulty_level():
    while True:
        print("Choose a difficulty level:")
        print("1. Easy level- Range:1-5, attempts:2")
        print("2. Intermediate level- Range:1-10, attempts:3")
        print("3. Hard level- Range:1-20, attempts:5")
        try:
            choice=int(input("Enter difficulty level of your choice-(1|2|3): "))
            if choice in [1,2,3]:
                return choice
            else:
                print("Enter a valid number from1,2,3 ")
        except:
            print("Invalid difficulty levelll ")

       
def guess_game():
    while True:
        difficulty=difficulty_level()
        if difficulty==1:
            lower_bound,upper_bound,max_attempts=1,5,2
        elif difficulty==2:
            lower_bound,upper_bound,max_attempts=1,10,3
        else:
            lower_bound,upper_bound,max_attempts=1,20,5


        rand_num=random.randint(lower_bound,upper_bound)
        attempts=0
       
        while attempts<max_attempts:
            try:
                guess_num=int(input(f'enter a number beatween {lower_bound} and {upper_bound} :'))
                

            except ValueError:
                print("Invalid input, try someother number")
                continue
           

            if guess_num<lower_bound or guess_num>upper_bound:
                print(f"you number is not in the range of {lower_bound} and {upper_bound} ")
            else:
                attempts+=1
                if(guess_num<rand_num):
                    print("Try entering some higher num: ")
                
                if(guess_num>rand_num):
                    print("Try entering some lower num: ")
                
                else:
                    print(f"Congrats!You won nothing for guessing correct num{rand_num}")
                    break
            
        print(f'total attempts: {attempts}')
        play_again=input("If you want to play again? (yes/y):  ").lower()
        if(play_again not in ['yes','y']):
            print("Thanks for playing! Have a great day!")
            break
        else:
            print(f"You have reached maximum num of attempts{max_attempts}. The correct num was {rand_num}")
if __name__=="__main__":
    guess_game()       
