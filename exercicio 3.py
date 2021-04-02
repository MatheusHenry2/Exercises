print('1 para converter c para f')
print('2 para converter f para c')
print('3 para converter c para k')
print('4 para converter k para c')
print('5 para converter c para r')
print('6 para converter r para c')
opcao = int(input('Informe sua opcao  :'))

while opcao < 1 or opcao> 6:
    opcao = int(input('Informe sua opcao  :'))

if opcao == 1:
    c = float(input('Informe a temperatura em celsius'))
    f = (c * 1.8) + 32
    print(f'A temperatura fah {f}')
elif opcao == 2:
    f = float(input('Informe a temperatura fahhrenit'))
    c = 5 / 9 * (f - 32)
    print(f'A temperatura em celsius : {c}')
elif opcao == 3:
    c = float(input('Informe a temperatura em celsius'))
    k = c + 273.15
    print(f'A temperatura em kelvin: {k}')
elif opcao == 4:
    k = float(input('Informe a temperatura kkelvin:'))
    c = (k - 275.15)
    print(f'A temp em celsius {c}')
elif opcao == 5:
    c = float(input('Informe a temperatura em celsius'))
    r = (c + 273.15) * 1.8
    print(f'O VALOR em rankine: {r}')
elif opcao == 6:
    r = float(input('Informe a temperaaturaa rankine:'))
    c = (k - 275.15)
    print(f'O valor eem celsius :{c}')