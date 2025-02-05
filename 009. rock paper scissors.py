import random
print("")
print("**************** Welcome to Python Rock-Paper-Scissors Game ****************")
choice_set = ("Rock","Paper","Scissors")
p_s = c_s = 0
while True:
    print("")
    p_c = input("Enter Your Move (Rock/Paper/Scissors): ").capitalize()
    if p_c not in choice_set:
        print("Invalid Move!")
        continue
    c_c = random.choice(choice_set)
    if p_c == c_c:
        print(f"Your Choice: {p_c}")
        print(f"Computer Choice: {c_c}")
        print("It's a Tie!")
    elif p_c == "Rock" and c_c == "Scissors":
        print(f"Your Choice: {p_c}")
        print(f"Computer Choice: {c_c}")
        print("You Win!")
        p_s += 1
    elif p_c == "Paper" and c_c == "Rock":
        print(f"Your Choice: {p_c}")
        print(f"Computer Choice: {c_c}")
        print("You Win!")
        p_s += 1
    elif p_c == "Scissors" and c_c == "Paper":
        print(f"Your Choice: {p_c}")
        print(f"Computer Choice: {c_c}")
        print("You Win!")
        p_s += 1
    else:
        print(f"Your Choice: {p_c}")
        print(f"Computer Choice: {c_c}")
        print("You Lose!")
        p_s += 1
    print("")
    if not input("Do You Want to Try Again? (y/n): ").lower() == "y":
        break
print("")
print(f"******************* Your Score: {p_s:02} || Computer Score: {c_s:02} *******************")
print("**************************** Thanks for Playing! ***************************")
print("")
