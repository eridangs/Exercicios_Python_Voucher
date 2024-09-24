import random
class RPG:

    def AtaqueJogador(self,player,enemy):
        enemy.HP -= player.Ataque
        print(f'Sua vida:{player.HP}\nVida do inimigo:{enemy.HP}')

    def AtaqueInimigo(self,player,enemy):
        player.HP -= enemy.Ataque
        print(f'Sua vida:{player.HP}\nVida do inimigo:{enemy.HP}')

    def DefesaAleatoria(self,player,enemy):
        sorte = random.randint(1,100)
        if  sorte >= 50:
            print("Você ataca!")
            self.AtaqueJogador(player,enemy)

            print("Inimigo reage!")

            player.HP -= (enemy.Ataque*player.Defesa)
            print(f'Sua vida:{player.HP}\nVida do inimigo:{enemy.HP}')
            print("Você se defendeu parcialmente do ataque!")

        else:
            print("Você ataca!")
            enemy.HP -= (player.Ataque*enemy.Defesa)
            print(f'Sua vida:{player.HP}\nVida do inimigo:{enemy.HP}')
            print("Inimigo se defendeu do seu ataque!")

            print("Inimigo reage!")

            player.HP -= (enemy.Ataque*player.Defesa)
            print("Você se defendeu parcialmente do ataque!")
            print(f'Sua vida:{player.HP}\nVida do inimigo:{enemy.HP}')

    def UsarPocao(self,player):
        print("Poções do inventário: ")
        for pocao, quantidade in player.Inventario.items():
                print(f'{pocao} - {quantidade} unidades')
        pocao = input(f"Qual poção deseja usar? ")
        pocao = pocao.upper() 
        
        if pocao == "RESTAURAÇÃO":
            if player.Inventario["Restauração"] >= 1:
                player.Inventario["Restauração"]-= 1
                print("Você recuperou 100 HP!")
                player.HP += 100
            else:
                print("Essa poção acabou.")

        elif pocao == "VIDA":
            if player.Inventario["Vida"] >= 1:
                player.Inventario["Vida"] -= 1
                print("Você recuperou 500 HP!")
                player.HP += 500
            else:
                print("Essa poção acabou.")      
                 
        elif pocao == "DE VOLTA A BATALHA":
            if player.Inventario["De volta a batalha"] >= 1:
                player.Inventario["De volta a batalha"] -= 1
                print("Você recuperou 200 HP!")
                player.HP += 200
            else:
                print("Essa poção acabou.")
        
        if player.HP > player.Max_hp:
            player.HP = player.Max_hp

    def Final_do_jogo(self,player,enemy):
        if player.HP <= 0:
            print("Você perdeu para o inimigo!\nFIM")
            exit()
        if enemy.HP <= 0:
            print("Você derrotou o inimigo!!!\nFIM")
            exit()

    