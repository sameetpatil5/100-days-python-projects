import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like in your password\n"))
nr_symbols=int(input("How many symbols would you like in your password\n"))
nr_numbers=int(input("How many numbers would you like in your password\n"))

# Easy Level
# password=""
# for e in range(1, nr_letters+1):
#     password+=random.choice(letters)
# for e in range(1, nr_symbols+1):
#     password+=random.choice(symbols)
# for e in range(1, nr_numbers+1):
#     password+=random.choice(numbers)
# print(password)

password_list=[]
password=""
for e in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for e in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
for e in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
for length in range(0, nr_letters+nr_symbols+nr_symbols):
    password+=str(password_list[length])
print(f"Your Password is {password}")