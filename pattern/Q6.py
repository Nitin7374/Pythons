# X X X X X X X X X
#   X X X X X X X
#     X X X X X
#       X X X 
#         X

n =9
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i*2):
        print("X",end=" ")
    print()