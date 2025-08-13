#          X
#       X  X  X
#     X X  X  X X
#   X X X  X  X X X
# X X X X  X  X X X X

n =6
for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i*2):
        print("x",end=" ")
    print()