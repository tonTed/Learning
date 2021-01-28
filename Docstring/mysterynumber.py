from random import randint
from sys import exit
import logging

logging.basicConfig(level=logging.DEBUG)

NUMBER_MAX = 100
MYSTERY_NUMBER = randint(1, NUMBER_MAX)
TRYS = 5
TRYS_PERFORMED = 0

logging.debug(f"Mystery number: {MYSTERY_NUMBER}")

while TRYS_PERFORMED < TRYS:
    selected_number = input(f"You have {TRYS - TRYS_PERFORMED} tries left\nSelect a number between 1 and {NUMBER_MAX}: ")
    if not selected_number in [str(nb) for nb in range(NUMBER_MAX + 1)]:
        continue
    elif int(selected_number) == MYSTERY_NUMBER:
        print(f"Congrats you find the right number in {TRYS_PERFORMED + 1} tries!!")
        exit()
    elif int(selected_number) < MYSTERY_NUMBER:
        print(f"The number {selected_number} is smaller than the mystery number")
    else:
        print(f"The number {selected_number} is bigger than the mystery number")
    TRYS_PERFORMED += 1
print(f"You loose :(. The right number was {MYSTERY_NUMBER}")



