name=input("enter the string ")
results=""
for char in name:
    if char.isupper():
        results+=char.lower()
    else:
        results+=char.upper()
print(results)
    


# name = input("enter the string: ")
# results = ""

# for char in name:
#     if char.isupper():
#         results += char.lower()   # convert to lowercase
#     elif char.islower():
#         results += char.upper()   # convert to uppercase
#     else:
#         results += char           # keep other characters same

# print("Toggled string:", results)
