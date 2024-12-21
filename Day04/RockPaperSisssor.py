paper="✋"
scissors="✌️"
rock="✊"

game_images=[rock, paper, scissors]

user_ans=int(input("What do you choose?\n 0 = Rock\n 1 = Paper\n 2 = Scissors\n"))
if user_ans>2:
    print("You may have entered wrong value!\nPlease try again.")
    exit()
else:
    print(f"You Chose: {game_images[user_ans]}")

import random
computer_ans=random.randint(0,2)
print(f"Computer chose: {game_images[computer_ans]}")

print(f"Your choice {game_images[user_ans]}  vs. Computer choice {game_images[computer_ans]} :")

if user_ans==computer_ans:
    print("Its a Draw")
elif user_ans==0 and computer_ans==1:
    print("You Lose")
elif user_ans==0 and computer_ans==2:
    print("You Win")
elif user_ans==1 and computer_ans==0:
    print("You Win")
elif user_ans==1 and computer_ans==2:
    print("You Lose")
elif user_ans==2 and computer_ans==0:
    print("You Lose")
elif user_ans==2 and computer_ans==1:
    print("You Win")
else:
    print("Its impossible to get this bro wtf")