# length of list

cities =["mumbai","pune","chennai","noida","gurgoan"]
heroes =["akshya","salman","shahrukh","ajay","govinda"]

def len_of_list(list):
    print(len(list))

len_of_list(cities)
len_of_list(heroes)

# print the list item in same line using function

actors =["akshya","salman","shahrukh","ajay","govinda"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(actors)    

# print factorial 

def cal_fact(n):
    fact =1
    for i in range(1,n+1):
        fact *= i
        print(fact)
cal_fact(6)        

# convert usd into inr

def convert_usd(usd):
    inr = usd *83
    print(usd,"usd =", inr,"INR")

convert_usd(50)   

# even odd

number= int(input("enter the number "))

def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"

result = even_odd(number)  

print(result)