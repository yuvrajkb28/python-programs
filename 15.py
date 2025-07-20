# strong number

num=int(input("enter the number "))
sum=0
temp=num
while num>0:
    r=num%10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if temp==sum:
    print("its strong number ")
else:
    print("its not strong number ")

# num=int(input("enter the number "))
# sum=0
# while num>0:
#     r=num%10
#     fact=1
#     for i in range(1,r+1):
#         fact=fact*i
#         sum=sum+fact
#         num=num//10
# if num==sum:
#     print("its strong number ")
# else:
#     print("not strong number ")



    
