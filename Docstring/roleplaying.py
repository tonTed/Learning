from random import randint
import logging
from sys import exit

logging.basicConfig(level=logging.DEBUG)

PLAYER_LIFE = ENEMY_LIFE = 50
PLAYER_POTION = 3

while True:
    choice = input("Would you like to attack (1) or use a potion (2)? ")
    if choice != "1" and choice != "2":
        print(f"###  {choice != '1'} ======== {choice != '2'}  ###")
        continue
    elif choice == "1":
        ENEMY_LIFE -= randint(5, 10)
    elif choice == "2" and PLAYER_POTION <= 0:
        print("You have no more potions!!")
        continue
    elif choice == "2":
        PLAYER_LIFE += randint(15, 50)
        PLAYER_POTION -= 1
    else:
        logging.warning(f"Bad entry :: {choice} type: {type(choice)}")
        continue

    if ENEMY_LIFE <= 0:
        print("You win the game!!!")
        exit()
    else:
        PLAYER_LIFE -= randint(5, 15)

    if PLAYER_LIFE <= 0:
        print("You loose the game!!!")
        exit()
    else:
        print(f"❤️You have {PLAYER_LIFE} point of life\n❤️The enemy have {ENEMY_LIFE} point of life")







