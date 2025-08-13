# store folllowing word meaning in a python dictionary
dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figure"]
    
}
print(dict)

#  you are given a list of subjects for students
# assume one classroo"m is required for 1 subjects
# how many classroom are needed by all student

students ={
    "python","java","c++","python","javascript",
    "java","python","java","c++","c"
}

print(students)
print(len(students))

# wap to enter marks of 3 students from the  users and
# store them in a dictinary, start with an empty dictionary
#  and add one by one . use subject name as key and marks
#  as value 

dict={}

x =int(input("enter marks of math: "))
dict.update({"math":x})

x =int(input("enter marks of eng: "))
dict.update({"eng":x})

x =int(input("enter marks of comp: "))
dict.update({"comp":x})

print(dict)


# figure out a way to store 9 & 9.0 as saprate value in
# the set (you can take help of build-in datatype)

values={
    ("float",9),
    ("int",9.0)
}
print(values)