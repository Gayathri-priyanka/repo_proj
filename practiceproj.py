import random
def guess_game():
    while True:
        lower_bound=int(input("enter the LOWER bound for your game: "))
        upper_bound=int(input("enter the UPPER bound for your game: "))
        rand_num=random.randint(lower_bound,upper_bound)
        attempts=0
        while True:
            try:
                guess_num=int(input(f'enter a number beatween {lower_bound} and {upper_bound} :'))
            except ValueError:
                print("Invalid input, try someother number")
                continue
            attempts+=1
            if guess_num<lower_bound or guess_num>upper_bound:
                print(f"you number is not in the range of {lower_bound} and {upper_bound} ")
            elif(guess_num<rand_num):
                guess_num=int(input("Try entering some higher num: "))
            elif(guess_num>rand_num):
                guess_num=int(input("Try entering some lower num: "))
            else:
                print(f"Congrats!You won nothing for guessing correct num{rand_num}")
                break
        print(f'total attempts: {attempts}')
        play_again=input("If you want to waste your time again? (yes/y): ").lower()
        if(play_again not in ['yes','y']):
            print("Good Decision!!Go do some userful work")
            break
if __name__=="__main__":
    guess_game()       
