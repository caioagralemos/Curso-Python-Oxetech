import pygame as pg
import os
import random
from classes.cano import Cano
from classes.passaro import Passaro
from classes.chao import Chao

pg.init()

alturaTela = 800
larguraTela = 500
tela = pg.display.set_mode((larguraTela, alturaTela))

imgCano = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'pipe.png')))
imgFundo = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bg.png')))
imgBase = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'base.png')))
imgPassaro = [
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird1.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird2.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird3.png'))),
]

pg.font.init()
fontePontos = pg.font.SysFont('SF Pro', 45)

def desenharTela(tela, passaros, canos, chao, pontos):
    tela.blit(imgFundo, (0,0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = fontePontos.render(f'Pontos: {pontos}', 1, (255,255,255))
    tela.blit(texto, (larguraTela - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pg.display.update()

def main():
    passaros = [Passaro(230,350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pg.display.set_mode((larguraTela,alturaTela))
    pontos = 0
    relogio = pg.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
                pg.quit()
                quit()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()

        for passaro in passaros:
            passaro.mover()
        chao.mover()

        adicionarCano = False
        removerCanos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionarCano = True
            cano.mover()
            if cano.x + cano.canoTopo.get_width() <0:
                removerCanos.append(cano)
        
        if adicionarCano:
            pontos += 1
            canos.append(Cano(600))
        for cano in removerCanos:
            canos.remove(cano)
            
        for i,passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y <0:
                passaros.pop(i)
                
        desenharTela(tela,passaros,canos,chao,pontos)
        

if __name__ == '__main__':
    main()    