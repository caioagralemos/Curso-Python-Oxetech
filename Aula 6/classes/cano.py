import pygame as pg
import os
import random

imgCano = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'pipe.png')))

class Cano:
    distancia = 200
    velocidade = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.posTopo = 0
        self.posBase = 0
        self.canoTopo = pg.transform.flip(imgCano,False,True)
        self.canoBase = imgCano
        self.passou = False
        self.definirAltura()

    def definirAltura(self):
        self.altura = random.randrange(50,450)
        self.posTopo = self.altura - self.canoTopo.get_height()
        self.posBase = self.altura + self.distancia
    
    def mover(self):
        self.x -= self.velocidade

    def desenhar(self, tela):
        # blit é o renderizador
        tela.blit(self.canoTopo, (self.x,self.posTopo))
        tela.blit(self.canoBase, (self.x,self.posBase))

    def colidir(self, passaro):
        passaroMask = passaro.getMask()
        topoMask = pg.mask.from_surface(self.canoTopo)
        baseMask = pg.mask.from_surface(self.canoBase)

        distanciaTopo = (self.x - passaro.x, self.posTopo - round(passaro.y))
        distanciaBase = (self.x - passaro.x, self.posBase - round(passaro.y))

        topoPonto = passaroMask.overlap(topoMask, distanciaTopo)
        basePonto = passaroMask.overlap(baseMask, distanciaBase)

        if basePonto or topoPonto:
            return True
        else:
            return False