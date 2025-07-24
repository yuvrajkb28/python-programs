# finding duplicate character in string

# Find duplicate characters using count()
string = input("Enter a string: ")
checked = []

for char in string:
    if char not in checked and string.count(char) > 1:
        print(char, "is duplicate")
        checked.append(char)
