import random

print("Hello!")
user_name = input("What's your name? ")
print("Let's play a game ", user_name, "!", sep="")
print("I am going to choose a number between 1 and 100 and you are going to guess it.")

random_number = random.randint(1, 100)
not_guessed = True

while not_guessed:
    user_guess = int(input("Guess a number: "))
    if user_guess > random_number:
        print("Too high!")
    elif user_guess < random_number:
        print("Too low!")
    else:
        print("You guessed it, well done!")
        break
