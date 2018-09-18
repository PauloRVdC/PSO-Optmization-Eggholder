from particula import Particula
from funcao import eggHolder
from copy import copy
import random

PARTICULAS = 80

def geraParticula():
    x1 = random.uniform(-512,512)
    x2 = random.uniform(-512,512)
    vel = random.uniform(0,1)
    particula = Particula(x1,x2,vel)
    return particula

class Enxame:
    def __init__(self):
        self.particulas = []
        self.memoria = [0,0]

    def createEnxame(self):
        for i in range(PARTICULAS):
            self.particulas.append(geraParticula())
            if eggHolder(self.memoria) > eggHolder(self.particulas[i].posicao):
                self.memoria = copy(self.particulas[i].posicao)