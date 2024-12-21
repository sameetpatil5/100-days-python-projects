print("Welcome to Python Pizza Deliveries!\n")
size=input("What size pizza do you want? S, M, or L\n")
add_pepperoni=input("Do you want pepperoni? Y or N\n")
extra_cheese=input("Do you want extra cheese? Y or N\n")
bill=0
# small pizza 15
# medium pizza 20
# large pizza 25

# pepperoni for small 2
# pepperoni for medium and large 3

# extra cheese any pizza 1
if size=="S":
    bill=bill+15  
elif size=="M":
    bill=bill+20
else:
    bill=bill+25
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
    bill=bill+1
else:
    bill=bill
print(f"Your final bill is ${bill}")