class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first+'.'+last+'@company.com'

    @property                      
    def email(self):
        return ('{}.{}@company.com'.format(self.first,self.last))

    @property   
    def fullname(self):
        print('{} {}'.format(self.first,self.last))

    def apply_raise(self):
        self.pay =  int(self.pay * self.raise_amt)

    @classmethod
    def set_raise(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split()
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
        
class Developer(Employee):

       
    def __init__(self,first,last,pay,lang):
        super().__init__(first,last,pay)
        self.lang = lang    
        #Employee.__init__(self,first,last,pay)

class Manager(Employee):

    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

emp = Employee('Kumar', 'Krishnappa',20000)        
dev = Developer('Thimma', 'rayan', 900000, 'python')
mgr = Manager('Kumar', 'Krishnappa',200000,[dev])

import datetime

my_date = datetime.date(2016,7,12)
print(Employee.is_workday(my_date))

print(emp.raise_amt)
Developer.set_raise(1.05)
print(dev.raise_amt)
Manager.set_raise(1.1)
print(mgr.raise_amt)
print(dev.lang)
print(emp.email)
emp1 = Employee.from_string('lakshmamma Krishnappa 15000')
print(emp1.email)




