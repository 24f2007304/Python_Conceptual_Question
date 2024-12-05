n = int(input("Enter the a number:"))
adsNum = abs(n)
rev = adsNum % 10
adsNum = adsNum //10
while adsNum>0:
    r = adsNum % 10
    adsNum = adsNum // 10
    rev = rev*10 + r
if (n>0):
    print(rev)
else:
    print(rev - 2*rev)
    # print(rev - 2*rev) Here there will be to get  mineus sign we go through rev(1-2) by taking common rev
