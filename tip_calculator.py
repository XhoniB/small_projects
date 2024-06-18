print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 5, 10, 12, 15 or 20? "))
people = int(input("How many people to split the bill?"))

new_bill = bill * (1 + tip/100)

result = (new_bill / people)
#result = round(result, 2)
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")
