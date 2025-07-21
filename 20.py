# lcd of number

num1=int(input("enter the num1 "))
num2=int(input("enter the num2  "))
l1,l2=num1,num2
while num2>0:
    r=num1%num2
    num1=num2
    num2=r
    gcd=num1
lcd=(l1*l2/gcd)
print(lcd)
print(gcd)
