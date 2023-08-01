import random
def guess_game():
    lower_bound=1
    upper_bound=10
    rand_num=random.randint(lower_bound,upper_bound)
    attempts=0
    while True:
        try:
            guess_num=int(input('enter a number beatween 1 and 10: '))
        except ValueError:
            print("Invalid input, try someother number")
            continue
        attempts+=1
        if(guess_num<rand_num):
            guess_num=int(input("Try entering some higher num: "))
        elif(guess_num>rand_num):
            guess_num=int(input("Try entering some lower num: "))
        else:
            print(f"Congrats!You won nothing for guessing correct num{rand_num}")
            break
    print(f'total attempts: {attempts}')
if __name__=="__main__":
    guess_game()       
