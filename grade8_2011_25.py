squares = [value**2 for value in range(1,2012)]
squares1=[]
result=0
for i in squares:
    j = squares.index(i)%4
    if j == 1 or j == 2:
        i1=-1*i
    if j == 3 or j == 0:
        i1=1*i
    squares1.append(i1)
for i in squares1:
    result=result+i
print(squares1)
print(result)


