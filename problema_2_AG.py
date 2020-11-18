import math
n=int(input('Intrroduceti numarul ='))
suma=0
for i in range (1, n+1):
    suma+=math.factorial(i)
print('suma este' , suma)
