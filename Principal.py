# Esse programa foi desenvolvido utilizando a linguagem de programação Python
print('')
#Menu
print('    Bem-vindo ao jogo Jokenpo!   ')
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
    print('   Jogador 1 entrou com um valor incorreto, logo, jogador 2 ganhou\n  Parabéns!!!')
    exit()
elif j2 >= 4:
    print('   Jogador 2 entrou com um valor incorreto, logo, jogador 1 ganhou\n  Parabéns!!!')
    exit()
#Empate
if j1 == j2:
    print('   O jogo empatou, mais sorte na próxima vez!!')
#Pedra por j1
if j1==1:
    if j2 == 2:
        print('   Jogador 2 ganhou, parabéns!!!')
    if j2 == 3:
        print('   Jogador 1 ganhou, parabéns!!!')
#Papel por j1
if j1 == 2:
    if j2 == 3:
        print('   Jogador 2 ganhou, parabéns!!!')
    elif j2 == 1:
        print('   Jogador 1 ganhou, parabéns!!!')
#Tesoura por j1
if j1 == 3:
    if j2 == 1:
        print('   Jogador 2 ganhou, parabéns!!!')
    elif j2 == 2:
        print('   Jogador 1 ganhou, parabéns!!!')
