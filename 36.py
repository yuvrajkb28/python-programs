# check an string as an angram

# name=input("enter the string 1 ")
# names=input("enter the string 2 ")
# if len(name)!=len(names):
#     print("its not an anagram ")
# else:
#       if sorted(name)==sorted(names):
#            print("its an angrama ")
#       else:
#            print("its not an angram ")  




name=input("enter the string 1 ")
names=input("enter the string 2 ")
if len(name)==len(names) and sorted(name)==sorted(names):
    print("its an angram ")
else:
    print("not an angram ")

