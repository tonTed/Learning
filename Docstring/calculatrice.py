
continue_ = True

while continue_:
    number_1 = input("Please enter a first number: ")
    number_2 = input("Please enter a second number: ")
    if number_1.isdigit() and number_2.isdigit():
        print(f"The result of the addition of the number {number_1} with the number {number_2} is equal to {int(number_1) + int(number_2)}.")
        continue_ = False
    else:
        print("Please enter two valid numbers")