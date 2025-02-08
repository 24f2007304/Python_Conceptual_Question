class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c =c
        
    
    def Is_valid(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return f"Valid"
            
        return f"Invalid"
        
    def Side_Classification(self):
        if self.Is_valid() == "Valid":
            
            if self.a == self.b == self.c:
               return f"Equilateral"
        
            elif self.a == self.b or self.b == self.c or self.a == self.c:
               return f"Isosceles"
        
            else :
                return f"Scalene"
        
        else :
            return f"Invalid"
            
    
    def Angle_Classification(self):
        if self.Is_valid() == "Valid":
            
            sides = sorted([self.a, self.b, self.c])
            if (sides[0]**2 + sides[1]**2) > (sides[2]**2):
                return f"Acute"
                
            elif (sides[0]**2 + sides[1]**2) == (sides[2]**2):
                return f"Right"
                
            else:
                return f"Obtuse"
        
        else:
            return f"Invalid"
            
    
    def Area(self):
        if self.Is_valid() == "Valid":
            s = (self.a + self.b + self.c)/2
        
            Area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        
            return Area
        
        else:
            return f"Invalid"