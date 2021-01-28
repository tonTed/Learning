from pprint import pprint

continue_ = True

shopping_list = []

while continue_:
    print("""Choose one of the following five choices:
    \t1: Add an element in the list
    \t2: Remove an element in the list
    \t3: Display the list
    \t4: Empty the list
    \t5: Exit""")
    choice = input("\U0001F449 Your choice: ")
    if not choice.isdigit():
        continue
    if not int(choice) in range(1,6):
        print("Bad choice! \n")
        continue
    if choice == "5":
        break
    elif choice == "4":
        shopping_list.clear()
    elif choice == "3":
        pprint(shopping_list)
    elif choice == "2":
        to_remove = input("Enter the name of the element to remove: ")
        if to_remove in shopping_list:
            shopping_list.remove(to_remove)
        else:
            print("The element does not exist! \n")
            continue
    elif choice == "1":
        shopping_list.append(input("Enter the name of the element to append: "))
