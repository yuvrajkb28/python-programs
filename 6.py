# leap year or not
year =int(input("enter the year "))
if year%400==0:
    print("its leap year")
elif(year%4==0 and year%100!=0):
    print("its leap year")
else:
    print("its not leap year ")