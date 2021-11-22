def pula_linha():
    print(" ")


def logica(ponto_vitoria_jogador_um, ponto_vitoria_jogador_dois,jogador_um,jogador_dois,ponto_inicial):
    print("Quem é o vencedor dessa partida: ", jogador_um, "ou", jogador_dois)
    vencedor_partida = int(input("Digite o número do vencedor: "))
    print(" ")
    while vencedor_partida != 1 and vencedor_partida != 2:
        print("Por favor, digite apenas os numeros ", jogador_um, "ou ", jogador_dois)
        vencedor_partida = int(input("[1] ou [2]:  "))
    else:
        if vencedor_partida == 1:
            ponto_vitoria_jogador_um = ponto_inicial + ponto_vitoria_jogador_um
            print(" ")
            print("Pontos de vitoria do jogador ",jogador_um, " : ", ponto_vitoria_jogador_um)
            continua_jogo = int(input("Vamos continuar o jogo? Sim[5] / Não[7] "))
            print(" ")
            if continua_jogo == 5:
                logica(ponto_vitoria_jogador_um, ponto_vitoria_jogador_dois,jogador_um,jogador_dois,ponto_inicial)
            elif continua_jogo == 7:
                print(" ")
                print("Jogo finalizado")
            else:
                print(" ")
                print("Erro, digite um numero valido")
                logica(ponto_vitoria_jogador_um, ponto_vitoria_jogador_dois, jogador_um, jogador_dois, ponto_inicial)


        elif vencedor_partida == 2:
            ponto_vitoria_jogador_dois = ponto_inicial + ponto_vitoria_jogador_dois
            print("Pontos de vitoria do jogador ",jogador_dois, " : ", ponto_vitoria_jogador_dois)
            continua_jogo = int(input("Vamos continuar o jogo? Sim[5] / Não[7] "))
            print(" ")
            if continua_jogo == 5:
                logica(ponto_vitoria_jogador_um, ponto_vitoria_jogador_dois,jogador_um,jogador_dois,ponto_inicial)
            elif continua_jogo == 7:
                print(" ")
                print("Jogo finalizado")
            else:
                print(" ")
                print("Erro, digite um numero valido")
                logica(ponto_vitoria_jogador_um, ponto_vitoria_jogador_dois, jogador_um, jogador_dois, ponto_inicial)