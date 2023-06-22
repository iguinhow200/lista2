numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número inválido. O programa será encerrado.")
    exit()

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = (numero % 100) % 10

resultado = ""

if centenas > 0:
    if centenas > 1:
        resultado += f"{centenas} centenas"
    else:
        resultado += f"{centenas} centena"

    if dezenas > 0 and unidades > 0:
        resultado += ", "
    elif dezenas > 0 or unidades > 0:
        resultado += " e "
elif dezenas > 0:
    if dezenas > 1:
        resultado += f"{dezenas} dezenas"
    else:
        resultado += f"{dezenas} dezena"

    if unidades > 0:
        resultado += " e "

if unidades > 0:
    if unidades > 1:
        resultado += f"{unidades} unidades"
    else:
        resultado += f"{unidades} unidade"

print('resultado')
