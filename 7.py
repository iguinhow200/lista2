a=float(input('digite um numero '))
b=float(input('digite outro '))
c=float(input('digite mais um '))
if a > b and a > c :
    print(f'o maior numero é o {a}')

elif b > c and  b > a :
    print(f'o maior numero e o {b}')

elif c > a and c > b :
    print(f'o maior numero é o {c}')

if c < a and c < b:
    print(f'o menor numero e o {c}')
elif b < c and b < a:
    print(f'o menor numero e o {b}')
elif a < c and a < b :
    print(f'o menor numero e o {a}')

else:
    print('os numeros são iguais')