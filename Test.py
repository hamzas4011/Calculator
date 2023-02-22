
#Welcome to the tip calculator
#What was the total bill?
#What percentage tip would you like to give?
#How many people to split the bill?
#Each person should pay

print("Welcome to the tip calculator")
total_bill = float(input("Enter the total bill: "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
split_bill = int(input("How many people to split the bill: "))

each_person_bill = (round((total_bill/split_bill)) * (percentage_tip/100 + 1))
print (f"Each person has to pay: {each_person_bill}")







