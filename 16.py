# perfect number 

num=int(input("enter the number  "))
sum=0
for i in range(1,int(num/2)+1):
    if num%i==0:
        sum=sum+i
        
if num==sum:
    print("its perfect number  ")
else:
    print("its not perfect number ")
    