import random

escolhas = ['pedra', 'papel', 'tesoura']
vitorias_jogador = 0
vitorias_computador = 0

while True:
    escolha_jogador = input('Escolha pedra, papel ou tesoura: ').lower()

    if escolha_jogador not in escolhas:
        print('Opção inválida! Tente novamente.')
        continue

    escolha_pc = random.choice(escolhas)
    print("O computador escolheu:", escolha_pc)

    if escolha_pc == escolha_jogador:
        print('Empate! Escolha novamente.')

    elif escolha_pc == 'pedra' and escolha_jogador == 'papel':
        print('Você ganhou!')
        vitorias_jogador += 1

    elif escolha_pc == 'pedra' and escolha_jogador == 'tesoura':
        print('Você perdeu!')
        vitorias_computador += 1

    elif escolha_pc == 'papel' and escolha_jogador == 'pedra':
        print('Você perdeu :(')
        vitorias_computador += 1

    elif escolha_pc == 'papel' and escolha_jogador == 'tesoura':
        print('Você ganhou!')
        vitorias_jogador += 1

    elif escolha_pc == 'tesoura' and escolha_jogador == 'pedra':
        print('Você ganhou!')
        vitorias_jogador += 1

    elif escolha_pc == 'tesoura' and escolha_jogador == 'papel':
        print('Você perdeu :(')
        vitorias_computador += 1

    print("Placar: Você", vitorias_jogador, "-", vitorias_computador, "Computador")

    if vitorias_jogador == 3:
        print("Parabéns! Você venceu o jogo!")
        break  
    elif vitorias_computador == 3:
        print("O computador venceu o jogo!")
        break  


