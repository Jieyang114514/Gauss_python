list_a=[]
list_b=[]
list_c=[]
a = 3
b = 5
c = 7
d = 240
while a < 540:
    a = a+6
    if a >= d:
        list_a.append(a)
while b < 540:
    b = b+10
    if b >= d:
        list_b.append(b)
while c < 540:
    c = c+14
    if c >= d:
        list_c.append(c)
    
ac = set(list_a) & set(list_c)
ab = set(list_a) & set(list_b)
bc = set(list_c) & set(list_b)
sett = set(list_a + list_b + list_c)
total = list_a + list_b + list_c
repetition = ac & ab & bc
final = len(total) - len(sett) - len(repetition)
print(final)

