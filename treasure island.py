print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("\nBandits started chasing you!\n")
print("You have now encountered two paths !")
choice1 = input("Which direction do you wanna go left or right? ").lower()

if choice1 == "left":
    print("\nYou have reached a river")
    choice2 = input("What will you do swim or use the boat? ").lower()
    if choice2 == "boat":
        print("\nYou have now reached the Island, You must now choose a door, Red, Blue or Yellow? ")
        choice3 = input("What door will you choose? ").lower()
        if choice3 == "blue":

            print("/nCONGRATUALTION!!! YOU HAVE FOUND THE TREASURE!!!")
        elif choice3 == "red":
            print("Venomous Snakes attack you, You Died. GAME OVER!")
        elif choice3 == "yellow":
            print("You fell into a deep hole, You Died. GAME OVER!")
        else:
            print("The Bandits captured you. GAME OVER!")
    elif choice2 == "swim":
        print("Crocodiles started attacking you. You Died. GAME OVER!")
    else:
        print("The Bandits captured you. GAME OVER!")
elif choice1 == "right":
    print("\nThe lions have seen you and stated attacking, You Died. GAME OVER!")
else:
    print("\nThe Bandits captured you. GAME OVER!")

