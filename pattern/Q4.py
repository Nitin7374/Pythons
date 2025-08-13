# X X X X X
#   X X X X
#     X X X
#       X X
#         X

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print("X",end=" ")
    print()