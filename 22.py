# palindrome the string

name=input("enter the name  ")
a=name[::-1]
print(a)
if name==a:
    print("its palindrome ")
else:
    print("its not palindrome")