print("Welcome to tip calculator")
total_bill = input("What was the total bill? $")
per_tip = int(input("What percentage of tip would you like to give? 10, 12, or 15 "))
num_people = int(input("How many people to split the bill?"))
tip = float(per_tip)/100
total_tip = float(total_bill) * float(tip)
tip_per = float(total_tip)/int(num_people)
result = "{:.2f}".format(tip_per)
print(f"Each person should pay: ${result}")