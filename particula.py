from copy import copy

class Particula:
    def __init__(self,x1,x2,vel):
        self.posicao = [x1,x2]
        self.velocidadeX1 = vel
        self.velocidadeX2 = vel
        self.memoriaLocal = copy(self.posicao)