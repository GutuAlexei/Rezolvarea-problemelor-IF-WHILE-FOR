# cati dolaria primit mihai cand avea n ani (n<20)
n=eval(input('Varsta lui Mihai este = '))
s=1
c=1
if n<20:
    for i in range (1,n+1):
        c=c*2
        s+=c+i
    print('Mihai a primit ' , s ,'bani, cand avea' , n , 'ani' )
else:
    print('Nu se respecteaza conditia problemei')
#La ce varsta cadoul lui mihai era de 100$
s = 1
i = 0
c = 1
while s<=100:
    i=i+1
    c=c*2
    s+=c+i
print('Varsta la care cadoul era de 100$ este de ', i , 'ani')
