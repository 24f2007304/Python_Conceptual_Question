# Here we are finding Triangle is made are not by given Cooradinates

def distance(a,b,c,d):
    dis = ((((a-c)**2) +((b-d)**2))**0.5)
    return dis

def istriangle(max , a,b):
    if((a+b)>max):
        print("\n Triangle")
    else:
        print("\n Not a Triangle")

x1 = float(input(" Enter the first X-Coordinate :"))
x2 = float(input("Enter the Second X- Coordinate :"))
x3 = float(input("Enter the Third X-Coordinate :"))
y1 = float(input("Enter the first Y-Coordinate :"))
y2 = float(input("Enter the Second Y-Coordinate :"))
y3 =float(input("Enter the Third Y-Coordinate :"))

d1 = distance(x1,y1,x2,y2)
d2 = distance(x2,y2,x3,y3)
d3 = distance(x3,y3,x1,y1)

if(d1>d2):
    if(d1>d3):
        istriangle(d1,d2,d3) 
    else:
        istriangle(d3,d1,d2)
elif(d2>d3):
    istriangle(d2,d1,d3)
else:
    istriangle(d3,d2,d1)
    