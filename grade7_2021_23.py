a1 = 47023
count1 = 0
a = a1
while a > 26:
    a = (a+5)/3
    print(a)
    count1 = count1+1
    
a2 = 5227
a = a2
count2 = 0
while a > 26:
    a = (a+5)/3
    print(a)
    count2 = count2+1
    
a3 = 853
a = a3
count3 = 0
while a > 26:
    a = (a+5)/3
    print(a)
    count3 = count3+1
    
a4 = 1399
count4 = 0
a = a4
while a > 26:
    a = (a+5)/3
    print(a)
    count4 = count4+1
    
z = list(str(count1))+list(str(count2))+list(str(count3))+list(str(count4))
print(z)
count = (max(z))
print("n is " + count)