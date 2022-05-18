# choose your own adventure

name = input("Type your name: ")

print("Welcome", name , "to this adventure!")

answer = input("You are on a dirt road, and it has come to an end, \n and you can go"
               " left or right. Which way do you want to go? ").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across. \n"
                   "Type walk to walk around it or type swim to swim across ")

    if answer == "swim":
        print("You swam across and was eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and passed out")
    else:
        print("Not a valid option. Game over")
elif answer == "right":
    answer = input("You have come to a bridge, it looks wobbly \n"
                   "do you want to cross or walk back ")
    if answer == "walk":
        print("You go back and you got ambushed")
    elif answer == "cross":
        print("You crossed the bridge and you meet a stranger \n "
              "do you talk to them? yes or no ")
        if answer == "yes":
            print("You talked to the stranger and they granted your wishes")
        elif answer == "no":
            print("You ignored the stranger and they stab you with a spear. \n"
                  "you are dead. Game over")
        else:
            print("Not a valid option. Game over")
    else:
        print("Not a valid option. Game over")

else:
    print("Not a valid option. Game over")

print("Thank you", name, "for playing with us")


