#class !

#1.  class variables 
class Employee:
    raise_amount =  1.04 # <- class variable 
    num_of_employees = 0 
    def __init__(self, name, pay):
        self.name  = name
        self.pay = pay 

        Employee.num_of_employees += 1 # every time you make an instantce , the calss varaible will increament by 1 
    
    def apply_raise(self):
        self.pay  = self.pay * Employee.raise_amount # <- if you enter raise_amount , it will error out : variable is not defined
                                                    # you can also use self.raise_amount  
    
emp1= Employee('yihan', 100)
print(Employee.raise_amount)
print(emp1.raise_amount)    #  this still works. python will first check if "raise_amount" exists for instance 
# in this case it does not , so it will check if class has that atribute or not   

print (emp1.__dict__)
print(Employee.__dict__)

# then , if i change the class attrirbute :
Employee.raise_amount =  1.05
print(Employee.raise_amount)
print(emp1.raise_amount)  #1.05 

# if i on;y change the instance  attribute:
Employee.raise_amount = 1.04 # change back to original value
emp1.raise_amount  = 1.05
print(Employee.raise_amount) #1.04
print(emp1.raise_amount) #1.05 
print(emp1.apply_raise()) # but this will still use the 1.04 for raise amount because in your definition , 
# you used Employee.raise_amount instead of self.raise_amount 

###