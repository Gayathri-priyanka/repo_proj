import random
rand_num=random.randint(1,10)
guess_num=0

while guess_num!=rand_num:
    guess_num=int(input('enter a number beatween 1 and 10: '))
    if guess_num==rand_num:
        print("u guessed correct number")
        break
    else:
        print("try again")
