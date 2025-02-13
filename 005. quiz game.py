print("")
print("**************************************** Quiz Game ****************************************")
print("")
questions = ("01. What is the National Bird of Bangladesh?",
             "02. What is the National Animal of Bangladesh?",
             "03. What is the National Flower of Bangladesh?",
             "04. What is the National Fruit of Bangladesh?",
             "05. What is the National Fish of Bangladesh?")

options = (("A. Magpie Robin","B. Pigeon","C. Starling","D. Bulbul"),
           ("A. Chimpanzee","B. Buffalo","C. Rabbit","D. Royal Bengal Tiger"),
           ("A. Rose","B. Marigold","C. Water Lili","D. sunflower "),
           ("A. Mango","B. Jackfruit","C. Banana","D. Pomegranate"),
           ("A. Rui","B. Hilsa","C. Salmon","D. Tilapia"))

answers = ("A","D","C","B","B")
question_num = len(questions)
score = 0

for index in range(question_num):
    print(questions[index])
    for x in range(4):
        print(options[index][x])
    guess = input("Enter Your Answer (A,B,C,D): ").capitalize()
    while not (guess == "A" or guess == "B" or guess == "C" or guess == "D"):
        print("Invalid Option!")
        guess = input("Enter Your Answer (A,B,C,D): ").capitalize()
    if guess == answers[index]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"Correct Answer is: {answers[index]}")
    print("")
score = (score / question_num) * 100
print(f"************************************ Your Score: {score:.2f}% ***********************************")
