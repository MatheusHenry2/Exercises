hora = int(input('Informe a hora'))
minutos = int(input('Informe os minutos'))
segundos = int(input('Informe os segundos'))

if hora >= 0 and hora <=24 and minutos >=0 and minutos <=60 and segundos >=0 and segundos <=60:
    print(f'A Hora {hora}:{minutos}:{segundos} é valida')
else:
    print(f'A Hora {hora}:{minutos}:{segundos} é invalida')