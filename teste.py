from particula import Particula
from enxame import Enxame
from funcao import eggHolder
from random import uniform
from copy import copy

PARADA = 50
W = 1
P1 = 1.5
P2 = 1.4    

enxame = Enxame()
enxame.createEnxame()
print('Funcao: ', eggHolder(enxame.memoria), '\nParticula: ', enxame.memoria)

for i in range(PARADA):
    for j in range(len(enxame.particulas)):
        enxame.particulas[j].velocidadeX1 = W * enxame.particulas[j].velocidadeX1 + P1 * uniform(0,1) * (enxame.particulas[j].memoriaLocal[0] - enxame.particulas[j].posicao[0]) + P2 * uniform(0,1) * (enxame.memoria[0] - enxame.particulas[j].posicao[0])
        enxame.particulas[j].velocidadeX2 = W * enxame.particulas[j].velocidadeX2 + P1 * uniform(0,1) * (enxame.particulas[j].memoriaLocal[1] - enxame.particulas[j].posicao[1]) + P2 * uniform(0,1) * (enxame.memoria[1] - enxame.particulas[j].posicao[1])
        
        enxame.particulas[j].posicao[0] = enxame.particulas[j].posicao[0] + enxame.particulas[j].velocidadeX1
        if (enxame.particulas[j].posicao[0] > 512): enxame.particulas[j].posicao[0] = 512
        if (enxame.particulas[j].posicao[0] < -512): enxame.particulas[j].posicao[0] = -512

        enxame.particulas[j].posicao[1] = enxame.particulas[j].posicao[1] + enxame.particulas[j].velocidadeX2
        if (enxame.particulas[j].posicao[1] > 512): enxame.particulas[j].posicao[1] = 512
        if (enxame.particulas[j].posicao[1] < -512): enxame.particulas[j].posicao[1] = -512
        
        if eggHolder(enxame.particulas[j].posicao) < eggHolder(enxame.particulas[j].memoriaLocal):
            enxame.particulas[j].memoriaLocal = copy(enxame.particulas[j].posicao)

        if eggHolder(enxame.particulas[j].posicao) < eggHolder(enxame.memoria):
            enxame.memoria = copy(enxame.particulas[j].posicao)

    print('Funcao: ', eggHolder(enxame.memoria), '\nParticula: ', enxame.memoria)