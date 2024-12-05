
import math

PI = math.pi

def Circle_Area(r):
    area = round(PI*r**2 ,ndigits=2)
    return( area)

def Circle_Parameter(r):
    par = round(PI*2*r ,ndigits=2)
    return( par)

def Rect_Area(l,b):
    area = round(l*b, ndigits=2)
    return( area)

def Rect_Parameter(l,b):
    Para = round(2*(l + b) , ndigits=2)
    return( Para)
 
Shape = ''
while(Shape != 'exit'):
    print("\nSHAPES :\nRectangle\nCircle\nexit")
    Shape = input("Enter the Shape that You Want to find Area or Parameter : ")
    property = ''
    if(Shape == "Rectangle"):
        l = float(input("Enter the Length of Rectangle:"))
        b = float(input("Enter the Breath of Rectangle:"))
        while(property == ''):
            print("\nPROPERTIES\nArea\nParameter\ngoback")
            property = input("Enter The Property :")
            if(property == "Area"):
                print(f'The Area of Circle {Rect_Area(l,b)}')
            elif(property =="Parameter"):
                print(f'The Parameter of Circle {Rect_Parameter(l,b)}')
            elif(property=="goback"):
                break   
        
    elif(Shape == "Circle"):
        r = float(input("Enter the Radius :"))
        while(property == ''):
            print("\nPROPERTIES\nArea\nParameter\ngoback")
            property = input("Enter The Property   : ")
            if(property == "Area"):
                print(f'The Area of Circle  : {Circle_Area(r)}')
            elif(property =="Parameter"):
                print(f'The Parameter of Circle:  {Circle_Parameter(r)}')
            elif(property=="goback"):
                break 
        
    elif(Shape == "exit"):
          break