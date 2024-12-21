total_even=0
for number in range(0, 101, 2):
    total_even+=number
print(total_even)

# Other Approach
total_even=0
for number in range(0, 101):
    if number % 2 == 0:
        total_even+=number
print(total_even)