# check the Anagram
str1=input("enter the string 1 ")
str2=input("enter the string 2 ")
if len(str1)!=len(str2):
    print("its not an Anagram  ")
else:
    if sorted(str1)==sorted(str2):
        print("its Anagram ")
    else:
        print("its not Anagram  ")