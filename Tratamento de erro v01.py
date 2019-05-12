# EXERCICIO  ANTECESSOR E SUCESSOR (COM TRATAMENTO DE ERRO V01)

sair = ' '
sair1 = ' '

while True:
    try:
        n = int(input('digite um numero: '))

    except ValueError:
        print('Você digitou uma string, neste campo só é possivel digitar numeros!')
        sair = input('\nDeseja continuar S ou N?: ').upper()

        if sair == 'S':
            continue
        elif sair == 'N':
            break

        continue
    a = n - 1
    b = n + 1
    print('O antecessor é {} e o sucessor é {}'.format(a, b))
    sair1 = input('\ndigite S para sair do programa, ou C para continuar: ').upper()

    if sair1 == 'C':
        continue
    elif sair1 == 'S':
        break
