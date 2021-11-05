import random

randomNumber = random.randint(1,10)

while True:
    guess = int(input('write your guess 1 to 10: '))
    
    if randomNumber == guess:
        print("you got the right answer")
        break
    elif randomNumber > guess:
        print("increase your number")
    else:
        print("decrease your number")