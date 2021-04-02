ano = int(input('Informe o ano:'))
mes = int(input('Informe o mês'))
dia = int(input('Informe o dia'))

bissexto = 0

if ano < 1583:
    if ano % 4 == 0:
        bissexto = 1
    else:
        bissexto = 0

if ano % 400 == 0:
    bissexto = 1

if ano % 4 == 0 and ano % 100 != 0:
    bissexto = 1

if dia < 1 or dia > 31:
    print('Data inválida')
    quit()
if mes < 1 or mes > 12:
    print('Data inválida')
    quit()
if ano == 0 or ano < 0:
    print('Data inválida')
    quit()
if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30:
    print('Data inválida')
    quit()
if mes == 2 and bissexto != 0 and dia > 29:
    print('Data inválida')
    quit()
if mes == 2 and bissexto == 0 and dia > 28:
    print('Data inválida')
    quit()
if ano == 1582 and mes == 10 and dia > 4 and dia <=14:
    print('Data inválida')
    quit()

else:
    print(f'Parabéns a data {dia}/{mes}/{ano} é valida')

