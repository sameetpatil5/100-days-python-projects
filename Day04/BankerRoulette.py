names_string=input("Give me everybody's names, separated by a comma.\n")
names=names_string.split(', ')

# Method 1
# import random
# upper_limit=names.count(",")
# upper_limit+=1
# random_name=random.randint(0, upper_limit)
# print(f"{names[random_name]} has to pay the bill today")

#Method 2
import random
upper_limit=len(names)
random_name=random.randint(0, upper_limit-1)
print(f"{names[random_name]} has to pay the bill today")

#Method 3
# import random
# random_name=random.choice(names)
# print(f"{random_name} has to pay the bill today")