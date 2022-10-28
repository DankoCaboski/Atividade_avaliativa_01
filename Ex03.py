a=15000
b=45000
c=65000
cont = 0
while True:
    a=a*1.1
    b=b*1.05
    cont+=1
    if a>= b:
        print(f'A passará B em {cont} anos')
        break
cont=0
a=15000
while True:
    a=a*1.1
    c=c*1.025
    cont += 1
    if a> (c*1.23):
        print(f'A superará C em 23% em {cont} anos')
        break