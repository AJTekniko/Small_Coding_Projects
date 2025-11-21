print("Welcome to the tip calculator!")

#Ask user for bill total
bill_total = float(input("What was the total bill? $"))

#Ask user how much in tips will be paid
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

#Ask user how many people will pay
split = int(input("How many people to split the bill? "))

#produce result
payment_due = round(bill_total * (1 + tip / 100) / split, 2)

print(f"Each person should pay: {payment_due}")