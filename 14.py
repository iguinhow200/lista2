nota=float(input('digite a sua nota '))
aproveitamento=0
if nota<=4:
    aproveitamento='E'
elif nota>4 and nota <=6:
    aproveitamento='D'
elif nota>6 and nota <=7.5:
    aproveitamento='C'
elif nota>7.5 and nota<=9:
    aproveitamento='B'
elif nota>9 :
    aproveitamento='A'

print(f'a sua nota foi {nota} e o seu aproveitamento {aproveitamento} ')