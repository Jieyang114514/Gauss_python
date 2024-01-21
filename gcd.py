a = 100
b = 200
c = 0
if a<b:
    c = a
elif b<a:
    c = b
else:
    print(a)
    
while c>=1:
    if a%c==0 and b%c==0:
        print(c)
        break
    else:
        c=c-1
        
    