# armstrong number 
num=int(input("enter the number "))
x=len(str(num))
temp=num
sum=0
while num>0:
    r=num%10
    sum=sum+r**x
    num=num//10
if temp==sum:
    print("its armstrong number ")
else:
    print("its not armstrong number ")
