a = int(input('Informe o valor do A: '))
b = int(input('Informe o valor do B: '))
c = int(input('Informe o valor do C: '))

D = (b ** 2 - 4 * a * c)
x1 = (-b + D ** (1 / 2)) / (2 * a)
x2 = (-b - D ** (1 / 2)) / (2 * a)

print(f' 1 raiz : {x1:.1f} A OUTRA raiz {x2:.1f}')
