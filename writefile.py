with open("file.txt", "w") as f:
    text_in = input("Please write a message to the file: ")
    f.write(text_in)

print("Printing file data: ")

with open("file.txt", "r") as f:
    print(f.read())