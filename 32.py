# searching technique
list=[23,45,76,89]
target_Element=90
found=False
for i in range(len(list)):
    if target_Element==list[i]:
        print("its found ")
        break
else:
    print("not found   ")

