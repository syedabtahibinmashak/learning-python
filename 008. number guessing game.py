import random
print("")
print("******************* Welcome to Python Number Guessing Game *******************")
print("")
low = 1
high = 100
answer = random.randint(low,high)
wrong_guess = 0
while True:
    guess = input(f"Guess a Number between {low} and {high}: ")
    if not guess.isdigit():
        print("Please Input a Valid Integer!")
        continue
    guess = int(guess)
    if guess == answer:
        print("Correct Guess!")
        break
    elif guess < low or guess > high:
        print("Out of Range! Try Again!")
        wrong_guess += 1
    elif guess > answer:
        print("Too High! Try Again!")
        wrong_guess += 1
    elif guess < answer:
        print("Too Low! Try Again!")
        wrong_guess += 1
print("")
print(f"Your Wrong Guesses: {wrong_guess}")
print("")
print("**************************** Thanks for Playing! *****************************")
