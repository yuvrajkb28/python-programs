# count number of digits

num=int(input("enter the number  "))
count=0
while num>0:
    r=num%10
    count=count+1
    num=num//10
print(count)
