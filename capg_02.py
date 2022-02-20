# Lista formada por função anônima de acordo com caracteres de uma string
carac_especiais = [i for i in '!@#$%^&*()-+']
# Lista formada por função anônima contendo os 10 numerais
digitos = [str(i) for i in range(0, 10)]
# Lista formada por função anônima contendo todas as letras minúsculas com
# auxílio da função chr() que converte os algoritmos da tabela ASCII
minusculas = [chr(i) for i in range(97, 123)]
# Lista formada por função anônima contendo todas as letras maiúsculas com
# auxílio da função chr() que se converte os algoritmos da tabela ASCII
maisculas = [chr(i) for i in range(65, 91)]

senha = input('Digite sua senha: ')

#Lista contendo controles para cada tipo de variável avaliada na senha.
#Estão definidos como False, pois isso será importante para a análise feita no próximo laço de repetição

controles = [['char_especial', False], ['numeral', False],
             ['minusc', False], ['maiusc', False]]

#Verifica cada caractere presente na senha digitada.
#Em seguida verifica-se o caractere atual em cada uma das listas de parâmetros obrigatórios.
#Caso o caractere esteja presente em alguma dessas listas o controle daquela variável muda para True.
#E dessa forma aquela lista não é mais procurada, pois aquele parâmetro já foi atendido, a quantidade de vezes não é importante
#para a avaliação de atendimento da condição. Isso agiliza o código, impedindo operações desnecessárias.

for char in senha:
    if controles[0][1] == False:
        if char in carac_especiais:
            controles[0][1] = True
    if controles[1][1] == False:
        if char in digitos:
            controles[1][1] = True
    if controles[2][1] == False:
        if char in minusculas:
            controles[2][1] = True
    if controles[3][1] == False:
        if char in maisculas:
            controles[3][1] = True

#Definiu a variável cont, ela será usada para calcular o número de condições não atendidas na senha.
#Esse laço de repetição percorre a lista de controles e para cada parâmetro com o resultado False ele soma 1 na varíavel cont.
#Se ao final do laço de repetição anterior um parâmetro cntinua com o resultado False, significa que aquele parâmetro não foi atendido,
#logo aquele é um tipo caractere obrigatório a constar na senha e portanto no cálculo pedido.
cont = 0
for i in controles:
    if i[1] == False:
        cont += 1

#O trecho abaixo fornece o output indicando o número de caracteres que o usuário deverá acrescentar afim de obter uma senha forte.
#Caso não seja necessário a inserção de nenhum caractere o usuário receberá a mensagem: 'Sua senha já é forte'.

if len(senha) > 6 and cont == 0:
    print('Sua senha é forte!')
elif len(senha) < 6:
    if 6 - len(senha) > cont:
        print(6 - len(senha))
    else:
        print(cont)
else:
    print(cont)