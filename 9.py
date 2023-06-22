n1=float(input('digite um numero '))
n2=float(input('digite mais um numeoro '))
n3=float(input('por fim digite mais um numero '))

if n1>n2 and n1>n2 and n1>n3 and n2>n3 :
    print(f'a ordem decrescente é {n1} {n2} {n3}')

elif n2>n3 and n2>n3 and n1>n3 :
    print(f'a ordem decrescente é {n2} {n1} {n3}')

else:
    print(f'a ordem decrescente é {n3} {n2} {n1}')
