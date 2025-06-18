from math import sqrt
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = (b ** 2) - 4*a*c
if a == 0:
    print ('A = 0, portanto, não é uma equação de segundo grau!')
    exit()
elif delta >= 0:
    bhask1 = (-b + sqrt(delta)) / (2*a)
    bhask2 = (-b - sqrt(delta)) / (2*a)
    if bhask1.is_integer():
        bhask1_formatado = int(bhask1)
    else: 
        bhask1_formatado = bhask1
    if bhask2.is_integer():
        bhask2_formatado = int(bhask2)
    else:
        bhask2_formatado = bhask2
    if a.is_integer():
        a1 = int(a)
    else:
        a1 = a
    if b.is_integer():
        b1 = int(b)
    else:
        b1 = b
    if c.is_integer():
        c1 = int(c)
    else:
        c1 = c
    print ('A equação {}x² + {}x + {} tem as raízes:\n{}\n{}'.format(a1, b1, c1, bhask1_formatado, bhask2_formatado))
else:
    print ('Delta é menor de zero. Portanto, não tem raízes reais.')
