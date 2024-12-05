# Accept a positive integer n as input , where n>1 . Print Prime if n is an prime number and Notprime otherwise..
''' Here We Use the Flage Method in Prime Number Questions'''
def Prime_Number(num):
    flag = True # Here we use the method og flag
    if num >1:
        for i in range(2 ,num):
            if num%i == 0 :
                flag == False
                break
        if (flag == True):
            return("Prime")
        else:
            return("Not Prime")                
    
print(Prime_Number(44))