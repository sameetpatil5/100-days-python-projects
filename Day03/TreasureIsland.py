print("Welcome to Treasure Island. You mission is to find the treasure.")
print("Your mission is to find treasure!")
ans=input("Do you want to take left or right?").lower()
if ans=="left":
    ans=input("Do you want to swim or wait?").lower()
    if ans=="wait":
        ans=input("Which Door you want to choose?").lower()
        if ans=="red":
            print("You Won!")
        elif ans=="blue":
            print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
