from fractions import Fraction
x=int(input('Intrroduceti numarul z ='))
y=int(input('Intrroduceti numarul y ='))
z=int(input('Intrroduceti numarul z ='))
t=int(input('Intrroduceti numarul t ='))
s=Fraction(x,y)+Fraction(z,t)
p=Fraction(x,y)*Fraction(z,t)
print('suma este' , s)
print('produsul  este' , p)