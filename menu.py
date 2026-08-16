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