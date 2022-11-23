
from random import randint  #IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS
from time import sleep
cont = 0
separacao = ('=-' * 30)

while True:   #WHILE PRINCIPAL QUE VAI SER RESPONSÁVEL POR DEIXAR O PLAYER JOGAR MAIS DE UMA VEZ

    while True:     #WHILE RESPONSÁVEL POR CONFIGURAR OS JOGOS, MENU E DIFICULDADE
        print(separacao)
        print('Seja bem vindo ao jogo de adivinhação!!!')
        dificuldade = int(input('Escolha um nível de dificuldade.'
                                '\n1) Fácil (0-10)'
                                '\n2) Médio (0-100)'
                                '\n3) Difícil (0-1000)'
                                '\nSua escolha: '))

        if dificuldade >= 4:        #IF RESPONSÁVEL POR VALIDAR O NÍVEL QUE O JOGADOR ESCOLHEU
            print('Opção inválida! '
                  '\nPor favor digite uma Opção válida.')
            sleep(1.5) #I
        else:
            print('Carregando...')
        print(separacao)
        sleep(1.5)
        if dificuldade == 1:
            numero = randint(0, 10)
            break
        elif dificuldade == 2:
            numero = randint(0, 100)
            break
        elif dificuldade == 3:
            numero = randint(0, 1000)
            break

    while True:     #WHILE RESPONSÁVEL DE GUIAR O JOGADOR NOS SEUS PALPITES
        palpite = int(input('Qual número eu pensei? '))
        cont += 1

        if palpite > numero:
            print('Errou! Tente um número mais baixo ')
            sleep(1)
            print(separacao)
        elif palpite < numero:
            print('Errou! Tente um número mais alto')
            sleep(1)
            print(separacao)
        elif palpite == numero:
            print(f'ACERTOU! Parabéns, eu realmente pensei no número {numero}, como você adivinhou? ')
            print(f'Você precisou de {cont} tentativas')
            sleep(.5)
            print(separacao)
            sleep(1.5)
            break



    replay = str(input('Você deseja jogar de novo? [S/N] ')).strip().upper()[0]
    sleep(.7)
    if replay == 'N': #IF RESPONSÁVEL POR FINALIZAR O JOGO QUANDO O PLAYER NÃO QUER MAIS JOGAR
        sleep(.5)
        print(separacao)
        print('\nJogo finalizado! Obrigado por jogar :)\n')
        print(separacao)
        sleep(2)
        break

    elif replay == 'S':
        print('carregando...')
        sleep(1)
        cont = 0
        break
    else:
        while True:
            print('Opção inválida! '
                  '\nPor favor digite uma Opção válida.')
            print(separacao)
            sleep(2)
            replay = str(input('Você deseja jogar de novo? [S/N] ')).strip().upper()[0]
            sleep(.7)
            if replay == 'N' or replay == 'S':
                break


