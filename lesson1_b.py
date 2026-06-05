class Employee:
    def__init__(self,name,salary):
             self.name = NameError
             self.salary= slary
    
    def get_salary(self):
           return self.salary 
    
    def get_salary(self, salary):
           if salary > 0:
                  self.salary= salary
            else:
                  print("Invalid salary.")
    
    def add_bonus(self, bonus):
           if bonus > 0:
                  self.salary += bonus
            else:
                  print("Invalid bonus.")

    def display(self):
           print("Employee:" , self.name)
           print("salary:" , self.salary)
           print("---------------------")

e1= Employee("Jhon", 1000)
e1.display()

e1.add_bonus(50000)
print("After Bonus:"e1.get_salary())

e1.set_salary(-1000)
e1.set_salary(20000)
e1.display()

e2= Employee("Alex", 20000)
e2.display()
e2.add_bonus(1000)
print("after bous:" , e2.get_salary())

e2.set_salary(15000)
e2.display()



    
    
    