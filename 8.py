preco1=float(input('digite o primeiro preço'))
preco2=float(input('digite o preço do concorrente'))
if preco2 > preco1:
    print('opte pela primeira loja la esta mais em conta')
elif preco1 > preco2:
    print('opte pela loja concorrente o preço la esta mais barato')
else:
    print('compre onde você foi melhor atendido(a) o preço esta idem')