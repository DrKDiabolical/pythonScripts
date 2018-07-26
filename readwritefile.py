while True:
    # Prints the available commands to the user
    print("Please enter an action: ")
    print("type 'create' to create the file")
    print("type 'write' to write to the file")
    print("type 'read' to read the file")
    print("type 'exit' to exit")

    # Initial name for the created file
    file_name = "words.txt"

    # Prompts the user for input
    choice = input(": ")

    # Exits the script
    if choice == "exit":
        print("~ exiting\n")
        break

    # Creates the file for the user to manipulate with a user-chosen name
    elif choice == "create":
        file_name = input("Please enter a name for the file: ")
        file_name += ".txt"
        with open(file_name, "w") as f:
            print("~ File created\n")

    # Prompts the user to input text into the file
    elif choice == "write":
        with open(file_name, "w") as f:
            text_in = input("Please enter text into the file: ")
            f.write(text_in)
            print("~ Text entered\n")
    
    # Reads the file to the user
    elif choice == "read":
        with open(file_name, "r") as f:
            print(f.read() + "\n")

    # Calls invalid input
    else:
        print("~ Invalid input\n")