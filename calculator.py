# Add, subtract, multiply and divide functions
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

#Add the 4 functions into a dicitionary as the values. Keys = "+", "-", "/", "*"
calc = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Use the dict. op. to perform the calc.
def calculator_game():
  num1 = int(input("What's the first number?: "))
  for i in calc.keys():
    print (i)
  op = input("Pick an operation from the line above: ")
  num2 = int(input("What's the second number?: "))
  print(f"{float(num1)} {op} {float(num2)} = {float(calc[op](num1,num2))}")
  
  game_over = False
  while game_over == False:
    inp = input(f"Type y to continue calculating with {float(calc[op](num1,num2))}, or type n to exit. ")
    if inp == "y":
      num1 = calc[op](num1,num2)
      op = input("Pick an operation from the line above: ")
      num2 = int(input("What's the next number?: "))
    elif inp == "n":
      game_over == True
      print("\n" * 10)
      calculator_game()

calculator_game()



