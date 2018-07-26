while True:
    # Prints the available commands to the user
    print("Please enter an operation: ")
    print("For addition, enter 'add',")
    print("For subtraction, enter 'subtract',")
    print("For multiplication, enter 'multiply',")
    print("For division, enter 'divide',")
    print("To exit, please enter 'exit'.")

    # Prompts the user for input
    user_input = input(": ")

    # Exits the script
    if user_input == "exit":
        print("~ exiting\n")
        break

    # Preforms an addition operation for the user
    elif user_input == "add":
        num1 = float(input("~ Please enter a number: "))
        num2 = float(input("~ Please enter another number: "))
        print("The answer is " + str(num1 + num2) + "\n")

    # Preforms a subtraction operation for the user
    elif user_input == "subtract":
        num1 = float(input("Please enter a number: "))
        num2 = float(input("Please enter another number: "))
        print("The answer is " + str(num1 - num2) + "\n")

    # Preforms a multiplication operation for the user
    elif user_input == "multiply":
        num1 = float(input("Please enter a number: "))
        num2 = float(input("Please enter another number: "))
        print("The answer is " + str(num1 * num2) + "\n")

    # Preforms a division operation for the user
    elif user_input == "divide":
        num1 = float(input("Please enter a number: "))
        num2 = float(input("Please enter another number: "))
        print("The answer is " + str(num1 / num2 + "\n"))

    # Calls invalid input
    else:
        print("Error, unknown action" + "\n")