# Write the Python Code to Find the Area of Rectangle and Circle also Paramenter
# Apporach 1 (There will not any type of Menu)
PI =22/7

def Circle_Area(r):
    area = PI*r**2 
    return area

def Circle_Parameter(r):
    par = 2*PI*r
    return par

def Rect_Area(l,b):
    area = l*b
    return area

def Rect_Parameter(l,b):
    Para = 2*l + 2*b
    return Para

R = float(input("Enter the Radies :"))
print(f'Area of Circle{Circle_Area(R)}')
print(f'Parameter of Circle{Circle_Parameter(R)}')

l = float(input("Enter the Length of Rectangle:"))
b = float(input("Enter the Breadth of Rectangle:"))

print(f'Area of Rectangle{Rect_Area(l,b)}')
print(f'Parmetr of Reactangle{Rect_Parameter(l,b)}')