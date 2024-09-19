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
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("WELCOME TO TREASURE ISLAND")
print("YOUR MISSION IS TO FIND THE TREASURE")
choice1 = input("You are at a crossroad, where do you want to go? Left or Right\n").lower()
if choice1 == 'left':
    choice2 = input('You have come to a lake. There is an island in the middle of the lake.\n'
                    'Type "swim" to swim across or type "wait" to wait for the boat\n').lower()
    if choice2 == 'wait':
        choice3 = input("You have arrived at the island unharmed.\nThere is a house with 3 doors?"
                        "Red, Blue, Yellow.\nWhich one do you want to choose\n").lower()
        if choice3 == 'yellow':
            print('You Win!')
        elif choice3 == 'red':
            print('Burned by fire.\nGame Over.')
        elif choice3 == 'blue':
            print('Eaten by beasts.\nGame Over.')
        else:
            print('You choose a door that do not exist. Game Over.')
    else:
        print("Attacked by trout.\nGFame Over.")
else:
    print("Fall into a hole.\nGame Over.")
