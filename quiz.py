# Simple Quiz Program

score = 0

answer = input("What is 2 + 2? ")

if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What is the capital of Pakistan? ")

if answer.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score is:", score)