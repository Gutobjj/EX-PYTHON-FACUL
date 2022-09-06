#EXERCICIO-3-PYTHON

#Identificação = JOSE AUGUSTO DE JESUS FILHO RU: 3034202
print('Seja bem-vindo ao programa de Feijoada do JOSE AUGUSTO DE JESUS FILHO RU: 3034202')

#iP-função sleep
from time import sleep

def volumefeijoada():  #Estabelecer o volume da feijoada (ML)
    global valor_volume

    print('-.-' * 58)
    print('Menu Volume Feijoada')
    print('-.-' * 58)

#não estabelecer volumes em litros ex:(2l , 1,5l) - prox melhoria.2000
    try:
        volume = int(input('Selecione a quantidade desejada (ml): '))

    except:
        print('ERRO! Valor digitado é inválido!')
        sleep(1)
        print('Tente novamente!')
        return volumefeijoada()

    else:
        if volume >= 300 and volume <= 5000:
            valor_volume = volume * 0.08

        else:
            print('Não é aceito porções menores que 300ml ou maiores que 5L. Tente Novamente!')
            sleep(1)
            return volumefeijoada()

#opcao feijoada

def opcaofeijoada():
    global valor_opcao

    print('-.-' * 30)
    print('Selecione a opção de Feijoada')
    print('-.-' * 30)

    opcao = input('''B- Básica (Feijão + Paiol + Costelinha) 
P- Premium (Feijão + Paiol + Costelinha + Partes de Porco)
S- Suprema (Feijão + Paiol + Costelinha + Partes de Porco + Charque + Calabresa + Bacon)
--> ''').upper()

    if opcao == 'B':
        valor_opcao = 1.00

    elif opcao == 'P':
        valor_opcao = 1.25

    elif opcao == 'S':
        valor_opcao = 1.50

    else:
        print('Digite uma opção válida!')
        sleep(1)
        return opcaofeijoada()

#acompanhamento feijoada adicional

def acompanhamentofeijoada():
    global valor_adicional
    valor_adicional = 0

    while True:
        print('-=-' * 30)
        print('Deseja acompanhamento adcional:')
        print('-=-' * 30)

        adicional = input('''0- Não desejo acompanhamento adcional')
1- 200g de Arroz
2- 150g de farofa especial
3- 100g de couve cozida 
4- 1 laranja descascada ''')

        if adicional == '1':
            valor_adicional += 5.00

        elif adicional == '2':
            valor_adicional += 6.00

        elif adicional == '3':
            valor_adicional += 7.00

        elif adicional == '4':
            valor_adicional += 3.00

        elif adicional == '0':
            print('Encerrando pedido...')
            sleep(1)
            break

        else:
            print('Digite uma opção válida!')


#MAIN-PP

volumefeijoada()
opcaofeijoada()
acompanhamentofeijoada()

total = (valor_volume * valor_opcao) + valor_adicional

print(
    f'O valor a ser pago é (R$): {total:.2f} (Volume = {valor_volume:.2f} * Opção = {valor_opcao:.2f} + Acompanhamento = {valor_adicional:.2f})')

#Identificação = JOSE AUGUSTO DE JESUS FILHO RU: 3034202