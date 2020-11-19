a=int(input('Intrroduceti a='))
b=int(input('Intrroduceti b='))
c=int(input('Intrroduceti c='))
if ((a<b+c) and (b<a+c) and (c<a+b)):
    if (a==b and a==c and b==c):
        print('triunghi este echilateral')
    elif (a==b or a==c or b==c):
        print('triunghi este isoscel')
    else:
        print('este un triunghi scalen ')
else :
    print('Nu exista asa un triunghi')