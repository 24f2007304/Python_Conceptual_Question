def Multip_(a,b):
    if b ==0:
        return 0
    return a + Multip_(a,b-1)

print(Multip_(2,3))