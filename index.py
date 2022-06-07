import random

print('\nOlá, digite seus dados de acesso para poder efetuar um saque no caixa 24 horas.\n')

#Variaveis globais
balance = 1000
withdraw = 5
account_data = 0

cpf = int(input('Digite seu CPF: '))
password = int(input('Digite sua senha: '))

#Introdução ao bloco de sistemas
if (cpf == 123 and password == 123):
    print('Olá, seja muito bem vindo a sua conta')
    print('(1) Extrato\n(2) Sacar\n(3) Depositar\n(4) Fechar')
    account_data = int(input('Digite o que você deseja realizar: '))

if (account_data == 1):
    account_number = random.randint(1000,9999) #Gerar números aleatórios entre 1000 e 9999
    print('Número da conta:', account_number)
    print('Saldo: R$', balance)
    print('Saques disponíveis:', withdraw)

elif(account_data == 2):
    withdraw_ok = int(input('Digite o valor que você deseja sacar: '))
    if(withdraw_ok <= balance):
        balance = balance - withdraw_ok #Conta simples pra somar o valor da variavel balance depois de realizar o saque
        print('Você sacou R${} da sua conta.'.format(withdraw_ok))
        print('Agora você tem R${} disponível em conta.'.format(balance))
        withdraw = withdraw -1 #Conta simples pra saber quantos saques podem ser realizados
        print('Você só pode realizar mais {} saques da sua conta.'.format(withdraw))
    if(withdraw_ok >= balance): 
        print('Você não tem esse valor disponível na conta!')

elif(account_data == 3):
    deposit = int(input('Digite o valor que você deseja depositar: '))
    balance = deposit + balance #Conta simples pra saber o valor que tem na conta após depositar
    print('Você depositou R${} na sua conta com sucesso e ficou com R${} disponível na conta!'.format(deposit, balance))    

elif(account_data == 4):
    exit
else:
    print('Dados inválidos')
