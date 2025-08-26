# find the first non reapting characters

name=input("enter the string ")
for ch in name:
    if name.count(ch)==1:
     print(ch)
