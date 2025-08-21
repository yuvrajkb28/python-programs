# remove duplicate from an string

name=input("enter the string  ")
result=""
for ch in name:
    if ch not in result:
        result+=ch
print(result)
    