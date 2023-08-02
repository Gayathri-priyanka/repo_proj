import random
def guess_game():
    while True:
        lower_bound=int(input("enter the LOWER bound for your game: "))
        upper_bound=int(input("enter the UPPER bound for your game: "))
        rand_num=random.randint(lower_bound,upper_bound)
        attempts=0
        max_attempts=5
        while attempts<max_attempts:
            try:
                guess_num=int(input(f'enter a number beatween {lower_bound} and {upper_bound} :'))
                

            except ValueError:
                print("Invalid input, try someother number")
                continue
           

            if guess_num<lower_bound or guess_num>upper_bound:
                print(f"you number is not in the range of {lower_bound} and {upper_bound} ")
            elif(guess_num<rand_num):
                print("Try entering some higher num: ")
                attempts+=1
            elif(guess_num>rand_num):
                print("Try entering some lower num: ")
                attempts+=1
            else:
                print(f"Congrats!You won nothing for guessing correct num{rand_num}")
                attempts+=1
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
