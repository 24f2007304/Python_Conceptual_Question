# Dictonaries is accept key Value Pair'
''' Key Vlaues Cannot be Same it must '''

# Updating and Adding in the Dictonaries

Student = {"Name":"Alok Tiwari","Roll No.":24017740250}
Student["Father Name"]="Sunil Tiwari"
Student["Name"] = "Alok Kumar Tiwari"
print(Student)

# Get Method
''' Here we have get method that is call by dot.'''
print(Student.get("Name"))


''' There will be difficult to write to del'''
# Delete Method
del(Student["Father Name"])
print(Student)



''' How to accces value in nested dictonaries'''
# Nested Dictionaries we have Dictionarie inside a Dictionaries and inside Dictionarie we have List

DukanData = {"Company":{"Wipro":["LED","Wire"],"KEI":["Wire","Fans"]}}
print(DukanData["Company"]["Wipro"])
print(Student)
# Student.clear()
# print(Student) # It will clear all the Data in Student Dictionaries

# Copy Method

School = Student.copy()
print(School)

