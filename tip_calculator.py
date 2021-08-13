#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? $ ")
tip = input("What percentange tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
#Converting data types
bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)
#Each person should pay (150.00 / 5) * 1.12 = 33.6
amnt_with_tip = (bill_float / people_int) * (1 + (tip_int / 100))

#Format the result to 2 decimal places = 33.60
result = "{:.2f}".format(amnt_with_tip)
print(f"Each person should pay: ${result}")
