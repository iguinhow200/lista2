salario=float(input('digite o seu salario atual'))
aumento=0
if salario <= 280 :
    aumento=salario*0.2
elif salario > 280 and salario < 700:
    aumento=salario*0.15
elif salario>=700 and salario<=1500:
    aumento=salario*0.1
else:
    aumento=salario*0.05

salarionovo=salario+aumento

print(f'o seu salario inicia era {salario} o aumento foi de {aumento} e agora e {salarionovo} ')