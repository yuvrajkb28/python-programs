# check whether a character is vowel or constant

name=input("enter the string ")
list1=["a","e","i","o","u"]
for char in name.lower():
    if char in list1:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a constant ")
