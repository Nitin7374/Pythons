# # write into file
# f = open("demo.txt","w")
# data = f.write("this is used to write into file")
# print(data)
# print(type(data))

# with open file

with open("sample.txt","w") as f:
    data = f.write("this is data ")
    print(data)