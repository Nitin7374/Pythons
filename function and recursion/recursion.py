# def show(n):  
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# fact

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(5))

# rcusion in list

def print_list(list,ind=0):
    if(ind == len(list)):
        return
    print(list[ind])
    print_list(list,ind+1)

fruits =["mango","apple","litchi","banana"]

print_list(fruits)