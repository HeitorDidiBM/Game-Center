import random
import time

def jogar():
    while True:
        print('Bem-vindo(a) ao jogo de advinhar números')
        print('Um número de 0 a 100 vai ser sorteado, tente advinhar qual é.')

        max_attempts = 0
        while True:
            try:
                dif = int(input('Qual o nivel de dificuldade? (1)Fácil (2)Médio (3)Dificil'))
            except ValueError:
                print('Escolha qual sua dificuldade em NÚMEROS!')
                continue
            if dif == 1:
                print('Você tem 10 tentativas!')
                max_attempts = 10
                break
            elif dif == 2:
                print('Você tem 5 tentativas!')
                max_attempts = 5
                break
            elif dif == 3:
                print('Você tem 3 tentativas!')
                max_attempts = 3
                break

        numero = random.randint(1, 100)
        attempts = 0

        while attempts < max_attempts:
            try:
                tentativa = int(input('Escreva um número  '))
            except ValueError:
                print('Digite um número! Não uma letra!')
                continue
            
            if tentativa < 0 or tentativa > 100:
                print('É um número entre 1 e 100! Escreva nos padrões por favor!')
                continue

            attempts += 1
            if tentativa == numero:
                plural = 'tentativas' if attempts != 1 else 'tentativa'
                print('Acertou!')
                print(f'Você usou {attempts} {plural}')
                break

            remaining = max_attempts - attempts
            if remaining == 0:
                print('Você perdeu! Suas tentativas acabaram!')
                print(f'O número era {numero}')
                break

            if tentativa > numero:
                print('É um número menor, tente novamente.')
            else:
                print('É um número maior, tente novamente.')
            plural = 'tentativas' if remaining != 1 else 'tentativa'
            print(f'Você só tem {remaining} {plural}')
        while True:
            again = input('Quer jogar novamente? (s/n):  ').lower()
            if again == 's':
                break
            elif again == 'n':
                print('Obrigado por tentar, até a próxima!')
                print('Retornando ao Game Center...')
                time.sleep(1)
                return True
            else:
                print('Digite "s" ou "n"')
                continue
