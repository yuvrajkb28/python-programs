# find the duplicate elements in string

name=input("enter the string ")
result=""
for names in name:
    if name.count(names)>1 and names not in result:
        result+=names
    print(result)






# string = input("Enter a string: ")
# duplicates = ""

# for char in string:
#     if string.count(char) > 1 and char not in duplicates:
#         duplicates += char

# print("Duplicate characters are:", duplicates)

