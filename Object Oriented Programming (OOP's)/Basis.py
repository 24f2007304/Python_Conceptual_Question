class Student:
    roll_no = None  # There will be intialize the rollno.
    Name = None # There will be intialize the Name
    
    
s0 = Student()
s0.Name ="Alok Tiwari" #Dot Operator  Here we are updating the Name 
s0.roll_no = 2415014408247250 # Here we are updating the rollno.

print(s0.Name,s0.roll_no)

# Creating Another Object ..

s1 = Student()  # Here we are not updating any value for s1 of Name & Rollno.
print(s1.Name,s1.roll_no)

s2 = Student()
s2.Name = "Parth Tiwari"
s2.roll_no = 214508274
print(s2.roll_no , s2.Name)

s50 = Student()
s50.Name = "Asmita"
print(s50.Name,s50.roll_no)