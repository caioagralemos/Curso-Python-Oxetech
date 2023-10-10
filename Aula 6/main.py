import pygame as pg
import os
import random

pg.init()

alturaTela = 800
larguraTela = 500
tela = pg.display.set_mode((larguraTela, alturaTela))

imgCano = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'pipe.png')))
imgFundo = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bg.png')))
imgChao = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'base.png')))
imgPassaro = [
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird1.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird2.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird3.png'))),
]

pg.font.init()
fontePontos = pg.font.SysFont('SF Pro', 45)

class Passaro:
    imgs = imgPassaro

    rotacaoMax = 25
    velocidadeRotacao = 20
    tempoAnimacao = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contador_imagem = 0
        self.imagem = self.imgs[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 12

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura+50):
            if self.angulo < self.rotacaoMax:
                self.angulo = self.rotacaoMax
        else:
            if self.angulo > -90:
                self.angulo -= self.velocidadeRotacao
    
    def desenhar(self, tela):
        self.contagem_imagem += 1

        if self.contador_imagem < self.tempoAnimacao:
            self.imagem = self.imgs[0]
        elif self.contador_imagem < self.tempoAnimacao*2:
            self.imagem = self.imgs[1]
        elif self.contador_imagem < self.tempoAnimacao*3:
            self.imagem = self.imgs[2]
        elif self.contador_imagem < self.tempoAnimacao*4:
            self.imagem = self.imgs[1]
        elif self.contador_imagem >= self.tempoAnimacao*4 + 1:
            self.imagem = self.imgs[0]
            self.contador_imagem = 0