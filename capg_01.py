# O número de caracteres por linha é uma constante. Basta imprimir um número de espaços complementar ao número de asteriscos e concatenar o resultado

x = 6
for i in range(1, x + 1):
    print(' '*(x - i) + '*'*i)