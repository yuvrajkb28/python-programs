# prime number are not

num=9
count=0
if num>1:
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
                print("its prime number ")
    else:
                print("its not prime number  ")
            
        
