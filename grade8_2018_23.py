list=0
a=1
n=0
while list < 2018:
    if (n+1)%5==0:
        print(str(n))
        list=list+1
        n = n+1
    elif (n+2)%5==0:
        print(str(n))
        list=list+1
        n = n+1
    else:
        n = n+1
