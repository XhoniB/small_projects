import random

top_of_range = input("Type a number: ") # request the user to put in a number

if top_of_range.isdigit(): # if the user input was a digit
    top_of_range = int(top_of_range) # then we convert top_of_range into an integer

    if top_of_range <= 0: # if the number is negative or zero then the user has to type in another nr.
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0 # nr. of guesses in the beginning

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number: # if the guessed number is the random number then we print the next line
        print("You got it! \n")
        break
    elif user_guess > random_number: # if the guessed number is bigger than the random nr.
        print("You were above the number!")
    else: # if the guessed number is smaller than the random nr.
        print("You were below the number!")

print("You got it in", guesses, "guesses")

