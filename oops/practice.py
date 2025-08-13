# create student class that takes name and marks of 3 
# students as argument in constructor.then create a method
# to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def print_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg marks is: ",sum/3)    


s1=Student("suresh",[65,70,68])

s1.print_avg()

# Q2
# create account class with 2 attributes- balance and
# account no. create method for debit,credit and printing
# the balnce.

class Account:
    def __init__(self,bal, acc):
        self.balance =bal
        self.accountno =acc
        # debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs. ",amount,"was debited")
        print("total balance = ",self.get_balance())
        # credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs. ",amount,"was credited")
        print("total balance = ", self.get_balance())
        # balance method
    def get_balance(self):
        return self.balance 

acc1 =Account(10000,45238574554)
print(acc1.balance)
# print(acc1.accountno)
acc1.debit(500)
acc1.credit(1000)


        


        