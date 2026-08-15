import random
import time

def calculadora():
    operaçoes_validas = ['+', '-', '*', '/']

    print("Esta é sua calculadora")
    print("Calcule o que quiser entre +, -, * e /")
    print("=" * 50)
    while True:
        try:
            n1 = int(input("Escolha seu 1º número: "))
        except ValueError:
            print('Por favor, digite um número.')
            print()
            continue
        operacao = input("Escolha entre +(mais), -(menos), *(multiplicação) e /(divisão): ")
        if operacao not in operaçoes_validas:
            print('Não tem como usar isso de operação! Tente algo válido')
            print()
            continue
        try:
            n2 = int(input("Escolha seu 2º número: "))
        except ValueError:
            print('Por favor, digite um número.')
            print()
            continue
        if operacao == "*":
            print(f"{n1 * n2}")

        elif operacao == "/":
            try:
                print(f"{n1 / n2}")
            except ZeroDivisionError:
                print('Não tem como dividir qualquer número por zero. Tente outro.')
                time.sleep(2)
                print()
                continue
        elif operacao == "+":
            print(f"{n1 + n2}")

        elif operacao == "-":
            print(f"{n1} - {n2} = {n1 - n2}")
        while True:
            sair = input('Deseja usar novamente? "s" ou "n"  ')
            if sair == 'n':
                print('Ok, Encerrando...')
                time.sleep(1)
                return True
            elif sair == 's':
                print('Ok, iniciando novamente!')
                time.sleep(2)
                return False
            else:
                print('Digite algo valido!')
                continue
