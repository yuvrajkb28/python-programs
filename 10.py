# palindrome number

num=int(input("enter the number "))
pal=num
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
print(rev)
if pal==rev:
    print("its palindrome number ")
else:
    print("its not palindrome ")


