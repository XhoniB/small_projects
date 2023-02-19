print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer1 = input("What does CPU stand for? ").lower()
if answer1 == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer2 = input("What does GPU stand for? ").lower()
if answer2 == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer3 = input("What does RAM stand for? ").lower()
if answer3 == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer4 = input("What does PSU stand for? ").lower()
if answer4 == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

not_last_question = input("Did you like the quiz? ").lower()
if not_last_question == "yes":
    print("Thank you for your feedback!\n")
else:
    last_question = input("What should we do better? \n").lower()
    feedback = last_question
    if feedback != "":
        print("Your feedback: ")
        print(feedback + "\n")
        print("Thank you for your feedback!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%" + " of the questions correct!\n")