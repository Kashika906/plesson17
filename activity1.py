import random

playing = True
number = str(random.randint(0, 9))

print("I will generate a number from 0 to 9 and you have to guess the number one digit at a time. Give your best try!")

while playing:
    guess = input("Enter your guess: ")

    if number == guess:
        print("Congratulations! You guessed correctly.")
        print("The secret number was:", number)
        break
    else:
        print("Wrong guess. Try again.")