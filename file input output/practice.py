# # Q1
# f =open("practice.txt","w") 
# data= f.write("hi everyone\n we are learning file I/O\n using java\n i like programming in java")
# print(data)
# f.close()

# # Q2

# f= open("practice.txt", "r")
# data= f.read()

# newdata= data.replace("java","python")
# print(newdata)

# f= open("practice.txt","w")
# f.write(newdata)

# # Q3

# word= "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word)!= -1):
#         print("found")
#     else:
#         print("not found")

#         f.close()

# Q4
def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
         while data:
             data= f.readline()
             if(word in data):
                 print(line_no)
                 return
            
             line_no +=1

    return -1
check_line()

# Q5
count = 0
with open("practice2.txt","r") as f:
    data = f.read()
    
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1
print(count)     
