# By the Help of These we can iterate in the Text(Big) Files ..

f = open("MobileNumber.text","r")
s = f.readline()
flag = 0
# if s !='':
s =int(s)
if s == 9936903610:
    print("The Number is Found")
    flag = 1
        
if flag ==0:
    print("The Number is not Founded")
    
