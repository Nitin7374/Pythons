class A:
    # default constructor
    def __init__(self):
        pass
  
    # paramirized constructor 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        # print(self)
        # print("my name is nitin choudhary")
        
    def welcome(self):
            print("welcome to the college")

    def get_marks(self):
         return  self.marks        

A1 = A("nitin",75)
print(A1.name,A1.marks)

A2 = A("manish",70)
print(A2.name,A2.marks)

A1.welcome()

print(A1.get_marks())