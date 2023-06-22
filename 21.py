valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido.")
else:
    notas_disponiveis = [100, 50, 10, 5, 1]
    quantidades_notas = []

    for nota in notas_disponiveis:
        quantidade = valor_saque // nota
        quantidades_notas.append(quantidade)
        valor_saque -= quantidade * nota

    print("Quantidade de notas fornecidas:")
    for i in range(len(notas_disponiveis)):
        nota = notas_disponiveis[i]
        quantidade = quantidades_notas[i]
        if quantidade > 0:
            print(f"{quantidade} nota(s) de {nota} reais.")