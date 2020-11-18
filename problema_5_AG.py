n=int(input('Intrroduceti anul format din 4 cifre ='))
n =n-2000
if (n%12==1) :
    print('Esti sarpe')
elif  (n%12==2):
    print('Esti cal')
elif  (n%12==3):
    print('oaia')
elif  (n%12==4):
    print('Esti maimuta')
elif (n%12==5) :
    print('Esti cocos')
elif  (n%12==6):
    print('Esti caine')
elif  (n%12==7):
    print('Esti porc')
elif  (n%12==8):
    print('Esti sobolan')
elif (n%12==9) :
    print('Esti sobolan')
elif  (n%12==10):
     print('Esti bou')
elif  (n%12==11):
     print('Esti tigru')
elif  (n%12==0):
    print('Esti dragon')
else:
    print('eror')