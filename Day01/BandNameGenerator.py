print("Welcome to Band Name Generator\n")
city_name = input("What is the name of the city you grew up in?\n")
pet_name = input("What is the name your pet?\n")
fav_num = input("What is your favourite number?\n")
print("Your Band Name is: " + city_name + " " + pet_name + " " + fav_num + "\n")
x = input("Did you like it?\n" + "*Please anwer in terms of yes or no*\n")
if (x == "yes"):
    print("Yay you have got a new Band Name\n" + city_name + " " + pet_name + " " + fav_num + "is Rocking!!!\n")
else:
    print("Ohh! Lets try again..." + "Your new Band Name is: " + pet_name + " " + city_name + " " + fav_num +"\n")
y = input("Did you like it?\n" + "*Please anwer in terms of yes or no*\n")    
if (y == "yes"):
    print("Yay you have got a new Band Name\n" + pet_name + " " + city_name + " " + fav_num + "is Rocking now for sure!!!\n")
else:
    print("Sorry I couldn't come up with any better name")