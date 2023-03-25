#  regular methodes take instance as the first arguments : def add(self): ...
# class method will take class as the first argument 

class Employee:
    raise_amount =  1.04 
    def __init__(self, name, pay):
        self.name  = name
        self.pay = pay 
    
    def apply_raise(self):
        self.pay  = self.pay * Employee.raise_amount
    
    @classmethod
    def set_raise_amt(cls, amount): #here , class object is taken as the first argument , instead of the instances 
        cls.raise_amount = amount  

    @classmethod
    def from_string(cls, emp_str):  #using classmethod as an alternative constructor 
        name, pay = [emp_str.split('-')[0], int(emp_str.split('-')[1])]
        return cls(name,pay)
    
    @staticmethod
    def is_week_day(day): #static method does not take cls or instances as input 
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        else:
            return True
        
    

print(Employee.raise_amount)
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)

#even if you apply class method on instance, it will still later class attributes:
emp1 = Employee('Yihan',100)
emp1.set_raise_amt(1.1)
print(Employee.raise_amount) #1.1 


## using class methods as alternative contructor for instances 

#to create an instance, ususaly we do this :
emp1 = Employee('yihan',100)

# now, using class method, we can creat instance from a string:
emp2 = Employee.from_string('yihan-200')
print(emp2.name)
print(emp2.pay)


## Static method 
# static method does not take cls or instance as input 

import datetime
my_date = datetime.date(2016,7,11)
print (Employee.is_week_day(my_date))