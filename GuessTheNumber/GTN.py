import random, pyfiglet, os

os.system("cls")
print(pyfiglet.figlet_format("GuessTheNum"))

num = random.randint(1,10)

while True:
    guess = input("Your Guess(1-10): ")
    if guess == num:
        print(f"You have guessed it! The number was {num}")
    else:
        print("You were wrong. Try Again.")