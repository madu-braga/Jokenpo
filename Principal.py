# Esse programa foi desenvolvido utilizando a linguagem de programação Python

print('')
#início e enquanto
op = 'jogar'
print('    Bem-vindo ao jogo Jokenpo!   ')
while op == 'jogar':
# Menu
    print('        _ _ _ _ _ _ _ _ _')
    print('       |                 |')
    print('       |    JoKenPo!     |')
    print('       |                 |')
    print('       |   1 - pedra     |')
    print('       |   2 - papel     |')
    print('       |   3 - tesoura   |')
    print('       |_ _ _ _ _ _ _ _ _|')
    #Entrada de variável
    j1 = int(input('   Jogador 1, escolha uma opção: '))
    j2 = int(input('   Jogador 2, escolha uma opção: '))
    #Perda por erro
    if j1 >= 4:
        print('   Jogador 1 entrou com um valor incorreto, logo, jogador 2 ganhou, parabéns!!!')
    elif j2 >= 4:
        print('   Jogador 2 entrou com um valor incorreto, logo, jogador 1 ganhou, parabéns!!!')
    #Empate
    elif j1 == j2:
        print('   O jogo empatou, mais sorte na próxima vez!!')
    #Pedra por j1
    elif j1==1:
        if j2 == 2:
            print('   Jogador 2 ganhou, parabéns!!!')
        elif j2 == 3:
            print('   Jogador 1 ganhou, parabéns!!!')
    #Papel por j1
    elif j1 == 2:
        if j2 == 3:
            print('   Jogador 2 ganhou, parabéns!!!')
        elif j2 == 1:
            print('   Jogador 1 ganhou, parabéns!!!')
     #Tesoura por j1
    elif j1 == 3:
        if j2 == 1:
            print('   Jogador 2 ganhou, parabéns!!!')
        elif j2 == 2:
            print('   Jogador 1 ganhou, parabéns!!!')
    print('')
    op = str(input('   Para jogar novamente digite,\"jogar\": ')).lower()
    if op == 'jogar':
        print('')
    else:
        print('')
        print('   Agradeço a utilização desse programa e espero que tenha gostado!\n   Atenciosamente: Maria Eduarda Macedo Braga')
        exit()
