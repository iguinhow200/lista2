import math

a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau. O programa será encerrado.")
    exit()

b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais. O programa será encerrado.")
    exit()
elif delta == 0:
    raiz = -b / (2*a)
    print(f"A equação possui apenas uma raiz real: {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")