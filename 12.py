salariobruto=float(input('digite o seu salario'))
inss=0
if  salariobruto<=900 :
    inss=0
elif salariobruto >=900 and salariobruto < 1500:
    inss=salariobruto*0.05
elif salariobruto >=1500 and salariobruto <2500 :
    inss=salariobruto*0.2
elif salariobruto >= 2500:
    inss*0.2
salarioliquido=salariobruto-inss
print(f'o seu salario liquido no final do mes sera de {salarioliquido} e o desconto foi de {inss}')
