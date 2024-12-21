age = input("What is your current age?")
num = 90-int(age)
print("You have " + str(num*365) + " days, " + str(num*52) + " weeks, " + str(num*12) + " and months left.")
#Version2
age2 = input("What is your current age?")
age2_as_int = int(age)
years_remaining = 90 - age2_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} years, {weeks_remaining} weeks, {months_remaining} and months left."

print(message)