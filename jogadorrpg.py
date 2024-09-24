class Jogador:
    def __init__(self,nome):
        self.Name = nome
        self.HP = 1000
        self.Max_hp = 1000
        self.Ataque = 150
        self.Defesa = 0.5
        self.Inventario = {"Restauração":3,"Vida":1,"De volta a batalha":1}