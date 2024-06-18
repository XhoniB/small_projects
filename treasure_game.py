print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n")
if direction == ("left" or "Left"):
          wait_or_swim = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
          if wait_or_swim == ("wait" or "Wait"):
                    which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
                    if which_door == ("red" or "Red"):
                              print("It's a room full of fire. Game over.")
                    elif which_door == ("yellow" or "Yellow"):
                              print("You Won!")
                    elif which_door == ("blue" or "Blue"):
                              print("You got eaten by beasts. Game over.")
                    else:
                              print("You chose a door that doesn't exist. Game over.")
          else:
                    print("You get attacked by an angry trout. Game Over.") 
else:
          print("You fell into a hole. Game Over!")
