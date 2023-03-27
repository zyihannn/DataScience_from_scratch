
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first= first
        self.last = last
        self.email = first +'.' + last + '@email.com'
        self.pay = pay 

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    
class Developer(Employee):
    raise_amt = 1.1 #it will overwrite the class variable in Employee (1.04)

    def __init__(self, first,last,pay,prog_lang):
        super().__init__(first,last,pay) #this is equivalent to : self.first =... , self.last=... , defined in Employee class 
        self.prog_lang = prog_lang

emp1 = Developer('yihan','zhang',100,'python')
print(emp1.prog_lang)
print(emp1.fullname())

#print(help(Developer)) #check "Method resolution order" section 

emp1.apply_raise()
print(emp1.pay) #100*1.1 


print('-------------------------')

class Manager(Employee):
    
    def __init__(self, first,last,pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None :
            self.employees = []

        else:
            self.employees = employees 

        
    def add_emp(self, emp): #emp is an Employee object 
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print(f'---> {emp.fullname()}')

emp1 = Developer('yihan','zhang',100, 'python')
emp2 = Developer('maymay','',100, 'java')

mgr_1 = Manager('Sue','Smith',900, [emp1])
mgr_1.print_emp() 

mgr_1.add_emp(emp2)
mgr_1.print_emp() 

print('-------------------------')

print(isinstance(mgr_1, Manager))  #true
print(isinstance(mgr_1, Employee))  #true 
print(isinstance(mgr_1, Developer)) #False 

print(issubclass(Manager, Employee)) #true
print(issubclass(Manager, Developer)) #false 

