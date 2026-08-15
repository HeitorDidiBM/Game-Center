import random
import time

def jokenpo():
    while True:
        print('Bem-Vindo(a) ao pedra, papel e tesoura')
        desicion = input('Deseja Jogar? (S/N)').lower()


        if desicion == 's':
            try:
                jogada_player = int(input('Escolha entre pedra(1), papel(2), tesoura(3).  '))
            except ValueError:
                print('Escreva um numero!')
        elif desicion == 'n':
            print('Ok, encerrando...')
            time.sleep(1.5)
            break
        else:
            print('Escreva como esta pedindo por favor!')

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
                (f'Empate! O bot escolheu a mesma coisa! {jogada_bot}.')
            elif jogada_player == 1:
                print(f'Ganhou! O bot escolheu {jogada_bot}.')

        
jokenpo()