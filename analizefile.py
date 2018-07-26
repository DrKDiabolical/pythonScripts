print("Welcome to file analizer V0.3")
filename = input("Please enter a file name to analize: ")

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

def count_chars(text):
    return(len(text))

def count_alphabet(text):
    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100 * count_char(text, char) / len(text)
        print("{0} - {1}%".format(char, round(perc, 2)))

def count_word(text, word):
    count = 0
    words = text.split(" ")
    for w in words:
        if w == word:
            count += 1
    return count

def count_words(text):
    words = text.split(" ")
    return(len(words))

while True:
    with open(filename, "r") as f:
        text = f.read()

        print("Please enter a command:")
        print("enter 'word amount' to analize word amount")
        print("enter 'amount of word' to analize a certain word")
        print("enter 'character amount' to analize character amount")
        print("enter 'amount of character' to analize a certain character")
        print("enter 'alphabetical' to analize alphabetically")
        print("enter 'exit' to exit script")

        choice = input(": ")

        if choice == "exit":
            print("~ exiting...")
            break
        elif choice == "word amount":
            print("~ analizing word amount...")
            print("Amount of words: " + str(count_words(text)) + "\n")
        elif choice == "amount of word":
            word = input("Please enter a word to analize: ")
            print("~ analizing amount of " + word + " in file...")
            print("amount of " + word + ": " + str(count_word(text, word)) + "\n")
        elif choice == "character amount":
            print("~ analizing character amount...")
            print("amount of characters: " + str(count_chars(text)) + "\n")
        elif choice == "amount of character":
            char = input("Please enter a character to analize: ")
            print("~ analizing amount of " + char + " in file...")
            print("amount of " + char + ": " + str(count_char(text, char)) + "\n")
        elif choice == "alphabetical":
            print("~ analizing amount of characters alphabetically...")
            print(count_alphabet(text))