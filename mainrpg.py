from jogadorrpg import Jogador
from inimigorpg import Inimigo
from turnos_games import RPG



print("Seja bem vindo ao RPG game!\nDefenda sua vida e batalhe quantas vezes quiser com o inimigo.")
nome = input("Qual seu nome jogador? ")

game = RPG()
player = Jogador(nome)
enemy = Inimigo()

def Menu():
    print("1 - Atacar!\n2 - Defender!\n3 - Usar cura!")

while True:
    Menu()
    game.Final_do_jogo(player,enemy)
    acao = int(input(""))

    if acao == 1:
       print("Você deu o ataque!\n")
       game.AtaqueJogador(player,enemy) 
       print("")
       print("Inimigo reage!\n")
       game.AtaqueInimigo(player,enemy)
       print("")

    if acao == 2:
        game.DefesaAleatoria(player,enemy)

    if acao == 3:
        game.UsarPocao(player)

            
 
