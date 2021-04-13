#impotação
from random import randint
print()
#enquanto
op = 'jogar'
print('    Bem-vindo ao jogo Jokenpo!   ')
while op == 'jogar':
    f = True;
    while f == True:
#menu principal
        print('        _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        print('       |                             |')
        print('       |           JoKenPô!          |')
        print('       |                             |')
        print('       |   1 - Jogar contra o pc     |')
        print('       |   2 - Jogar contra um amigo |')
        print('       |   3 - Sair                  |')
        print('       |_ _ _ _ _ _ _ _ _ _ _ _ __ _ |')
        opm = int(input('   Escolha uma opção de jogo: '))
        if opm != 1 and opm != 2 and opm != 3:
            print()
            print('   Digite uma opção válida: ')
            f = True
        else:
            f = False
#sair
    if opm == 3:
        exit()
#jogar contra o computador
    elif opm == 1:
        sort = randint(1, 3)
        if sort == 1:
            j1 = 1
        elif sort == 2:
            j1 == 2
        else:
            j1 == 3
        print('        _ _ _ _ _ _ _ _ _')
        print('       |                 |')
        print('       |    JoKenPô!     |')
        print('       |                 |')
        print('       |   1 - pedra     |')
        print('       |   2 - papel     |')
        print('       |   3 - tesoura   |')
        print('       |_ _ _ _ _ _ _ _ _|')
        j2 = int(input('   Escolha uma opção: '))
#jogar contra um amigo
    else:
        print('        _ _ _ _ _ _ _ _ _')
        print('       |                 |')
        print('       |    JoKenPô!     |')
        print('       |                 |')
        print('       |   1 - pedra     |')
        print('       |   2 - papel     |')
        print('       |   3 - tesoura   |')
        print('       |_ _ _ _ _ _ _ _ _|')
        j1 = int(input('   Jogador 1, escolha uma opção: '))
        j2 = int(input('   Jogador 2, escolha uma opção: '))
#perda por erro
    if j1 >= 4:
        print('   Jogador 1 entrou com um valor incorreto, logo, jogador 2 ganhou, parabéns!!!')
    elif j2 >= 4:
        print('   Jogador 2 entrou com um valor incorreto, logo, jogador 1 ganhou, parabéns!!!')
#empate
    elif j1 == j2:
        print('   O jogo empatou, mais sorte na próxima vez!!')
#pedra por j1
    elif j1 == 1:
        if j2 == 2:
            print('   Jogador 2 ganhou, parabéns!!!')
        elif j2 == 3:
            print('   Jogador 1 ganhou, parabéns!!!')
#papel por j1
    elif j1 == 2:
        if j2 == 3:
            print('   Jogador 2 ganhou, parabéns!!!')
        elif j2 == 1:
            print('   Jogador 1 ganhou, parabéns!!!')
#tesoura por j1
    elif j1 == 3:
        if j2 == 1:
            print('   Jogador 2 ganhou, parabéns!!!')
        elif j2 == 2:
            print('   Jogador 1 ganhou, parabéns!!!')
#jogar novamente
    print()
    op = str(input('   Para jogar novamente digite,\"jogar\": ')).lower()
    if op == 'jogar':
        print()
    else:
        print()
        print('   Agradeço a utilização desse programa e espero que tenha gostado!\n   Atenciosamente: Maria Eduarda Macedo Braga')
        exit()
