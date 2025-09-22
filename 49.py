# find smallest element

# find the largest and smallest eleent in array

a=[12,56,34,90,14]
min=a[0]
for i in range(1,len(a)):
    if a[i]<min:
        min=a[i]
print(min)