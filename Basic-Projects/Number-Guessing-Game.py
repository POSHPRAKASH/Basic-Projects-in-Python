import random

num = random.randint(1, 100)
guess = None
attempts = 0

while guess != num :

    guess = int(input("Guess a Number between 1 and 100: "))

    if guess == num:
        print("Congratulations! You Won!")
    elif guess < num :
        print('Higher.....')
    elif guess > num :
        print('Lower.....')
    else :
        print('Error....Try Again....')
    attempts += 1
print('Number of Attempts = ',attempts)