class Student:
   def __init__(self,name,age):
     self.name= name 
     self.age = age

   def introduce(self):
      print(f"Hello, My name is {self.name} and i am {self.age} years old.")


student1 = Student("Nameerah" , 25)
student1.introduce()

student2 = Student("Samhita" , 15)
student2.introduce()

student3 = Student("Amelie", 17)
student3.introduce()

