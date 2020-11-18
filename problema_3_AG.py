m=int(input('Intrroduceti numarul m ='))
n=int(input('Intrroduceti numarul n ='))
while n%m==0:
    n=n//m
if n==1:
    print('n este puterea lui m')
else:
    print('n nu este puterea lui m')