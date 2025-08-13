nums=(4,5,7,86,4,99,77,3)
# x =int(input("enter x value: "))
x =77
i=0
while i < len(nums):
    if( nums[i]==x):
        print("x found at index :",i)
        i += 1
    