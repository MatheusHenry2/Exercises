a = int(input('Informe o 1 valor:'))
b = int(input('Informe o 2 valor:'))

if a > b:
    print(f' Ordem crescente {a} {b}')
elif b > a:
    print(f'Ordem crescente {b} {a}')
else:
    print(f' {a} {b} são iguais')
