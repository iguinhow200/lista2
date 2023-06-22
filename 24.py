numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida.")
    exit()

paridade = "par" if resultado % 2 == 0 else "ímpar"
sinal = "positivo" if resultado >= 0 else "negativo"
tipo = "inteiro" if resultado.is_integer() else "decimal"

print(f"O resultado da operação é: {resultado}")
print(f"O número é {paridade}, {sinal} e {tipo}.")