# frequency of number 
name=input("enter the name ")
d={}
for char in name.lower():
    if char in d:
        d[char]+=1
    else:
        d[char] = 1
print(d)