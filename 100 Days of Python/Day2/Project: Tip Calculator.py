# Tip Calculator

# This project should consist below:

# 1. Welcome prompt.
# 2. Question that saves the user input - "What's wat the total bill? ".
# 3. Question that saves the user input - "How much tip would you like to give? ".
# 4. Question that saves the user input - "How many people to split the bill? ".
# 5. Prompt how much each person should pay

print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill? "))
tip = int(input("How much tip (% of total bill) would you like to give? "))
amountOfPeople = int(input("How many people to split the bill? "))
totalAmount = (totalBill+(totalBill*(tip/100)))/amountOfPeople

print(f"Each person should pay: {totalAmount}")
