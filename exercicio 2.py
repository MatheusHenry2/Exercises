a = int(input('Informe o 1 valor:'))
b = int(input('Informe o 2 valor :'))
c = int(input('Informe o 3 valor'))

if a > b and a > c:
    if b > c:
        print(f'Ordem crescente {a} {b} {c}')
    if c > b:
        print(f'Ordem crescente {a} {c} {b}')
elif b > a and b > c:
    if a > c:
        print(f'Ordem crescente {b} {a} {c}')
    if c > a:
        print(f'Ordem crescente {b} {c} {a}')
elif c > a and c > b:
    if a > b:
        print(f'Ordem crescente {c} {a} {b}')
    if b > a:
        print(f'Ordem crescente {c} {b} {a}')

