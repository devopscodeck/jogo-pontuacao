from time import sleep
from funcoes import *


print("--------------------------------------")
print("|Bem vindo a tabela de apostas do UNO|")
print("--------------------------------------")
pula_linha()
jogador_um = input("Digite o nome do primeiro jogador: ")
jogador_um = jogador_um+"[1]"
jogador_dois = input("Digite o nome do segundo jogador: ")
jogador_dois = jogador_dois+"[2]"
ponto_vitoria_jogador_um = 0
ponto_vitoria_jogador_dois = 0

sleep(1)
print("... jogadores cadastrados com sucesso !!")
sleep(1)
pula_linha()
pula_linha()
print("----------------------------------------ATENÇÃO---------------------------------------------------")
print("Cada jogador será representado por um número", jogador_um, " e ", jogador_dois)
print("Basta digitar o número de cada jogador para confirmar de quem foi a vitória da partida ")
print("Todas as sessões serão calculadas, armazenadas e exibidas na tela quando solicitado.")
pula_linha()
sleep(10)
print("..")
sleep(1)
print("..")
sleep(1)
pula_linha()
print("Vamos comerçar..")
ponto_inicial = int(input("Defina o valor de pontos marcados a cada vitória: "))
logica(ponto_vitoria_jogador_um, ponto_vitoria_jogador_dois,jogador_um,jogador_dois,ponto_inicial)