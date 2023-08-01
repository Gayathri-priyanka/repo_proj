import random
rand_num=random.randint(1,10)
guess_num=int(input('enter a number beatween 1 and 10: '))
while guess_num!=rand_num:
    if(guess_num<rand_num):
        guess_num=int(input("Try entering some higher num: "))
    elif(guess_num>rand_num):
        guess_num=int(input("Try entering some lower num: "))
    else:
        print("You entered correct number")
        break

        
