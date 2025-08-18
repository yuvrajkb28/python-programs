# count vowels
name=input("enter the string ")
str=name.lower()
count=0
list1=["a","e","i","o","u"]
for char in name:
    if char in list1:
        count+=1
print(count)

# count for constant
name=input("enter the string ")
str=name.lower()
count=0
list1=["a","e","i","o","u"]
for char in name:
    if char not in list1:
        count+=1
print(count)

