# gcd of number 

num1=int(input("enter the num1 "))
num2=int(input("enter the num2  "))
while num2>0:
    r=num1%num2
    num1=num2
    num2=r
gcd=num1
print(gcd)