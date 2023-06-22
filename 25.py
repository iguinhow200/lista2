print("Responda as perguntas abaixo (sim ou não):")

pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

respostas_positivas = 0

if pergunta1.lower() == "sim":
    respostas_positivas += 1

if pergunta2.lower() == "sim":
    respostas_positivas += 1

if pergunta3.lower() == "sim":
    respostas_positivas += 1

if pergunta4.lower() == "sim":
    respostas_positivas += 1

if pergunta5.lower() == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("Classificação:", classificacao)