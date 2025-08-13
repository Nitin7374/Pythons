a = int(input("Entered first number "))
b = int(input("Entered second number "))
c = int(input("Entered third number "))

if(a >=b and a >=c):
    print("a is greater")
elif(b >=c):
    print("b is greater")
else:
    print("c is greater")