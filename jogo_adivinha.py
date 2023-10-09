import random

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            if(num <= 0 or num > 5):
                print('Digite apenas números entre 1 até 5')
                continue
        except(ValueError, TypeError):
                print('Digite apenas números inteiros.')
                continue
        else:
            return num

print("*********************************")
print("Bem vindo ao jogo de adivinhação.")
print("*********************************")

# Criando um número secreto.
numero_secreto = random.randint(1,5)
print(f'O numero secreto é: {numero_secreto}')
contador = 0
tentativas = 2

while(contador < 3):
    numero = leiaInt('Digite um número de 1 até 5:  ')
    if(numero == numero_secreto):
        print('*****************************')
        print(f'Parabéns, você acertou!!')
        print(f'O número era: {numero}')
        print('*****************************')
        break
    else:
        print(f'Numero errado,restam ==>  {tentativas} chances.')

    contador += 1
    tentativas -= 1




