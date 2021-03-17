print('\033[36mPrimeiro Trabalho de Lógica e fundamentos:''\033[m')
barras = '-------'
print(barras)
resultado = '\033[36mResultado:''\033[m'

#Primeiro exercício:
print('1. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).')
print(resultado)
parouimpar = int(input('Digite, um número inteiro:'))
if (parouimpar%2) == 0:
    print('O numero que você digitou é par')
else:
    print('O numero que você digitou é impar')
print(barras)

#Segundo exercicio:
print('2. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.')
print(resultado)
intoudec = float(input('Digite um número:'))
if (intoudec // 1 == intoudec):
    print('O numero que você digitou é inteiro')
else:
    print('O numero que você digitou é decimal')
print(barras)

#Terceiro Exercicio:
print('Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado\n'
      ' da operação deve ser acompanhado de uma frase que diga se o número é:'
      '\npar ou ímpar;'
      '\npositivo ou negativo;'
      '\ninteiro ou decimal.')
print(resultado)
print('Informe Dois Numeros diferentes de 0' )
primnum = float(input('Primeiro numero:'))
segnum = float(input('Segundo numero:'))
escolha = int(input('Qual operação você gostaria de realizar?Digite: \n"1" para soma\n"2" Para subtração\n"3" Para divisão'))
if escolha == 1:
    soma = primnum+segnum
    print('A soma dos dois Numeros é igual à {}'.format(soma))
    if (soma % 2) == 0:
        print('o numero {} é par'.format(soma))
    else:
        print('O número {} é impar'.format(soma))

    if soma < 0:
        print('negativo')
    else:
        print('positivo ')
    if soma//1 == soma:
        print('Inteiro')
    else:
        print('Decimal')
if escolha == 2:
    subtracao = primnum - segnum
    print('A divisão dos dois Numeros é igual à {}'.format(subtracao))
    if (subtracao % 2) == 0:
        print('o numero {} é par'.format(subtracao))
    else:
        print('O número {} é impar'.format(subtracao))

    if subtracao < 0:
        print('negativo')
    else:
        print('positivo ')
    if subtracao // 1 == subtracao:
        print('Inteiro')
    else:
        print('Decimal')

if escolha == 3:
    divisao = primnum / segnum
    print('A divisão dos dois Numeros é igual à {}'.format(divisao))
    if (divisao % 2) == 0:
        print('o numero {} é par'.format(divisao))
    else:
        print('O número {} é impar'.format(divisao))

    if divisao < 0:
        print('negativo')
    else:
        print('positivo ')
    if divisao // 1 == divisao:
        print('Inteiro')
    else:
        print('Decimal')
print(barras)

#Quarto exercicio:
print('Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:\n'
      '"Telefonou para a vítima?"\n'
      '"Esteve no local do crime?"\n'
      '"Mora perto da vítima?"\n'
      'Devia para a vítima?"\n'
      '"Já trabalhou com a vítima?"\n'
      'O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder \n'
      'positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".\n'
      ' Caso contrário, ele será classificado como "Inocente".')
print('Que comece o interrogatório. Faremos algumas perguntas sobre o crime. Não minta! Digite "1" se\n'
        'você confirma o pedido pela pergunta, ou "0" se for uma inverdade')
print(resultado)
primper = int(input('Telefonou para a vítima?'))
segper = int(input('Esteve no local do crime?'))
terper = int(input('Mora perto da vítima?'))
quarper = int(input('Devia para a vítima?'))
quinper = int(input('Já trabalhou com a vítima?'))
total = primper+segper+terper+quarper+quinper
if total == total==0 and total<2:
    print('Você é inocente')
elif total == 2:
    print('você é suspeito')
elif total == total>2 and total<5:
    print('Você é cumplice')
elif total > 5:
    print('Vocênão digitou os números corretamente')
else:
    print('você é assassino')
print(barras)

#Quinto exercicio:
print('Um posto está vendendo combustíveis com a seguinte tabela de descontos:\n'
      'Álcool:\n'
      'Até 20 litros, desconto de 3% por litro\n'
      'Acima de 20 litros, desconto de 5% por litro\n\n'
      'Gasolina:\n'
      'até 20 litros, desconto de 4% por litro\n'
      'acima de 20 litros, desconto de 6% por litro')
print('Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: \n'
      'A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina\n'
      ' é R$ 2,50 o preço do litro do álcool é R$ 1,90.')
print(resultado)
alcougas = str(input('Seja bem vindo!! Se você irá abastecer com alcool, digite [A], se prefere abastecer com Gasolina, digite [G]'))

quantia = int(input('Quantos Litros?'))
quantiagaso = quantia * 2.50
quantiaalcol = quantia * 1.90

if alcougas == 'a' or alcougas =='A':
    if quantia <= 20:
        print('O valor a ser pago é de R$ {}'.format(quantiaalcol*0.97))
    elif quantia > 20:
        print('O valor a ser pago é de R$ {}'.format(quantiaalcol*0.95))
    else:
        print('Digite algum valor')
if alcougas == 'g' or alcougas == 'G':
    if quantia <= 20:
        print('O valor a ser pago é de R$ {}'.format(quantiagaso*0.96))
    elif quantia > 20:
        print('O valor a ser pago é de R$ {}'.format(quantiagaso*0.94))
    else:
        print('você precisa abastecer alguma quantia')
print(barras)

#Sexto exercicio:
print('6. Uma fruteira está vendendo frutas com a seguinte tabela de preços:\n'
      '                 Até 5 Kg                Acima de 5 Kg\n'
      'morango         R$ 2,50 por Kg          R$ 2,20 por Kg\n'
      'Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg\n'
      'Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um \n'
      'desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade \n'
      '(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.')
print(resultado)
produtos = [("morango", 2.50, 2.20), ("maçã", 1.80, 1.50)]

while True:
    count = 0
    calculo_produto = 0
    finalizar = False

    produto = input("Por favor, informe o produto desejado(Morango ou Maçã):")

    for x in range(2):
        if produto.lower() == produtos[x][0]:
            count = x
            finalizar = True
            break
        else:
            if x == 1:
                finalizar = False
                print("Valor inválido.", produto)
    if finalizar:
        break
while True:
    try:
        peso = float(input("Por favor, informe o peso desejado:"))

        if peso > 0:
            break
        else:
            continue
    except ValueError:
        print("valor Invalido do peso.")
        continue
if peso <= 5 and peso > 0:
    calculo_produto = produtos[count][1] * peso

elif peso > 5:
    calculo_produto = produtos[count][2] * peso
    if peso > 8 or calculo_produto > 25:
        calculo_produto = (produtos[count][2] * peso) - ((produtos[count][2] * peso) * 10 / 100)

print("Valor a pagar:R$%.2f" % calculo_produto)
print(barras)

print('\033[36m ESSE FOI O MEU TRABALHO ^-^\n Espero que tenha gostado!''\033[m')
