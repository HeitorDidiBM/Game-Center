import random
import time
import calculadora



def menu():
    print('='*50)
    print('🎮BEM-VINDO(A) AO GAME CENTER!🎮'.center(45))
    print('='*50)
    time.sleep(0.5)
    print('\n=== Jogos ===')
    print('1 - Advinhador de Números')
    print('2 - Jokenpo')
    print('3 - Calculadora')
    print('='*30)
    print('Outras opções:')
    print('0 - Sair')

    try:
        print('='*30)
        açao = int(input('Oque quer fazer?  '))  
    except ValueError:
        print('Por favor, escreva em números')
        return False

    if açao == 1:
        print('Ok, iniciando Advinhador!')
        time.sleep(1)
        jogar()
    elif açao == 2:
        print('Ok, iniciando Jokenpo!')
        time.sleep(1)
        jokenpo()
    elif açao == 0:
        print('Encerrando...')
        time.sleep(1)
        return True
    elif açao == 3:
        print('Ok, iniciando calculadora!')
        time.sleep(1)
        calculadora.calculadora()

def jokenpo():
    while True:
        print('Bem-Vindo(a) ao pedra, papel e tesoura')

        try:
            jogada_player = int(input('Escolha entre pedra(1), papel(2), tesoura(3).  '))
        except ValueError:
            print('Escreva um numero!')
   
        jogada_bot = random.randint(1, 3)

        if jogada_bot == 1:
            jogada_bot = 'pedra'
        if jogada_bot == 2:
            jogada_bot = 'papel'
        if jogada_bot == 3:
            jogada_bot = 'tesoura'

        if jogada_bot == 'pedra':
            if jogada_player == 2:
                print(f'Ganhou! O bot escolheu {jogada_bot}.')
            elif jogada_player == 3:
                print(f'Perdeu! O bot escolheu {jogada_bot}.')
            elif jogada_player == 1:
                print(f'Empate! O bot escolheu a mesma coisa! {jogada_bot}.')

        if jogada_bot == 'papel':
            if jogada_player == 2:
                print(f'Empate! O bot escolheu a mesma coisa! {jogada_bot}.')
            elif jogada_player == 3:
                print(f'Ganhou! O bot escolheu {jogada_bot}.')
            elif jogada_player == 1:
                print(f'Perdeu! O bot escolheu {jogada_bot}.')

        if jogada_bot == 'tesoura':
            if jogada_player == 2:
                print(f'Perdeu! O bot escolheu {jogada_bot}.')
            elif jogada_player == 3:
                print(f'Empate! O bot escolheu a mesma coisa! {jogada_bot}.')
            elif jogada_player == 1:
                print(f'Ganhou! O bot escolheu {jogada_bot}.')
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
while True:
    sair = menu()

    if sair:
        break