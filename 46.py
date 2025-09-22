# pyraid structure

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
n = 5  # Number of rows

for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print stars with spaces
    for j in range(2 * i + 1):
        print("*", end="")

    # Move to next line
    print()

