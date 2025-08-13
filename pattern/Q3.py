#       X
#     X X
#   X X X
# X X X X

n =6
for i in range(1, n):
    for j in range(i, n-1):
        print(" ",end=" ")
    for k in range(i):
         print("X", end=" ")
    print()