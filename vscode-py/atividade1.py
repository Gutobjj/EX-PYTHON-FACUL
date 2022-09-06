#EXERCICIO-01-PYTHON

#Identificação = JOSE AUGUSTO DE JESUS FILHO RU: 3034202
print('Seja bem-vindo a loja do JOSE AUGUSTO DE JESUS FILHO RU: 3034202')

#guia_Valores.
valor = float(input('Insira o valor do produto: '))
quantidade = float(input('Insira a quantidade de produtos: '))

#se menor ou igual a 4, o desconto é de 0 (0%)
if quantidade <= 4:
   desconto = 0 
#se for entre 5  a 19, o desconto é de 0.03 (3%)
elif 5 <= quantidade <= 19:
   desconto = 0.03
#se for entre 20  a 99, o desconto é de 0.06 (6%)
elif 20 <= quantidade <= 99:
   desconto = 0.06
#se maior ou igual a 100, o desconto é de 0,10 (10%)
else:
   desconto = 0.10

sem_desconto = valor * quantidade
com_desconto = sem_desconto - sem_desconto * desconto

print('O valor SEM desconto é: R${:.2f}' .format(sem_desconto))
print('O valor COM desconto é: R${:.2f}' .format(com_desconto))

#Identificação = JOSE AUGUSTO DE JESUS FILHO RU: 3034202