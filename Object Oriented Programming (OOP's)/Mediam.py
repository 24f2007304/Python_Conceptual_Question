class Student:
    count =0  # It is not an Object it is an Class Attribute
    def __init__(self,rollno,name,Total): # __init__ is a special method in Python known as a constructor . That helps to construct the Classes
# It is Object Attribute
        self.rollno = rollno
        self.name = name
        self.Total = Total
        
    def display(self):
        print(self.rollno,self.name,self.Total)
        
    def result(self):
        if self.Total>120:
            print("Pass")
        elif self.Total <120 and self.Total>115:
            print("Compartement")
        else :
            print("Fali")        
    
s0  = Student(0, "Bhuvneshwar" ,123)
s0.display()
Student.count+=1
s0.result()

s1 =Student(1 ,"Adam Golf",100)
s1.display()
Student.count+=1
s1.result()

s2 = Student(2 ,"Pussa Margo Andrew",116)
Student.count+=1
s2.display()
s2.result()  # Here this will be given the specific behaviour of s2
print(f'Total Number Student:{Student.count}')