import pygame
from random import randint
import pyglet

vidPath = 'intro.mp4'
window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()


@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(-1, 49)


pyglet.app.run ()

pygame.init()

fundo = pygame.image.load('fundo.png')         #(carregando imagem de fundo: pista,agua e grama)
linhas = pygame.image.load('linhas_pista.png') #(carregando imagem das linhas da pista e criando a variavel linha)
carro10 = pygame.image.load('carro10.png')      #(carregando imagens dos carros e definindo as variaveis carros)
ambulancia = pygame.image.load('ambulancia.png')
policia00 = pygame.image.load('policia00.png')
policia01 = pygame.image.load('policia01.png')

arvore01 = pygame.image.load('arvore01.png') #carregando as imagens das arvores e definindo-as
arvore02 = pygame.image.load('arvore02.png')
arvore03 = pygame.image.load('arvore03.png')
arvore01d = pygame.image.load('arvore02.png')
arvore02d = pygame.image.load('arvore03.png')
arvore03d = pygame.image.load('arvore01.png')
i = 0
x = 369      #(posição do carro do jogador eixo x) limite 195x 527meio 369
y = 480         #(posição do carro do jogador eixo y)  #pos_policia00_x = 526 equivale a pos_x = 526
pos_policia00x = 515                                   #pos_policia00_y = 1200  equivale a pos y
pos_policia00y = 600
pos_policia01x = 223
pos_policia01y = 500               #= pos policia = pos_x = posição da eixo X e Y do carro de policia 00)
pos_ambulanciay = 2000
pos_ambulanciax = 310

pos_arvore_x1 = 30; pos_arvore_y1 = -300
pos_arvore_x2 = 30; pos_arvore_y2 = -200
pos_arvore_x3 = 30; pos_arvore_y3 = -100
pos_arvore01dx = 600; pos_arvore01dy = -120
pos_arvore02dx = 700; pos_arvore02dy = -240
pos_arvore03dx = 830; pos_arvore03dy = -360

pos_linha_x = 0           #posição da linha da pista no eixo x ( não varia)
pos_linha_y = -600        #posição da linha da linha da pista no eixo y
velocidade = 20
tempo = 0
tempo_seg = 0
vel_carros = 60
vel_linha = 60
pontos = 0
fonte = pygame.font.SysFont('arial black',20)   # fonte do texto "tempo" ( arial black tamanho 20)
texto = fonte.render(" Tempo: ",True,(255,255,255),(0,0,0))  # texto (cor letra)
pos_texto = texto.get_rect()   #posição do texto

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Iniciando o Jogo ")

janela_aberta = True
while janela_aberta :
        pygame.time.delay(5) # atualização de frames + 31.25 do relógio = 1000 milissegundos (1 segundo )
        for i in range(0, 3):
            if pos_arvore_y1 < 600 or pos_arvore01dy < 600:
                pos_arvore_y1 = pos_arvore_y1 + 1; pos_arvore01dy = pos_arvore01dy +1
            else:
                pos_arvore_y1 = randint(-423, -343) ; pos_arvore01dy = pos_arvore_y1
            if pos_arvore_y2 < 600 or pos_arvore02dy < 600:
                pos_arvore_y2 = pos_arvore_y2 + 1
                pos_arvore02dy = pos_arvore02dy +1
            else:
                pos_arvore_y2 = randint(-423, -200); pos_arvore02dy = -200
            if pos_arvore_y3 < 600 or pos_arvore03dy < 600:
                pos_arvore_y3 = pos_arvore_y3 + 1; pos_arvore03dy = pos_arvore_y3
            else:
                pos_arvore_y3 = randint(-423, -80); pos_arvore_03dy = pos_arvore_y3

            if pos_linha_y < 0:  # Testa a condição se a posição da pista no eixo y é menor que 0
                pos_linha_y = pos_linha_y +1  # caso seja é incrementado +1 na posição do eixo y
            else:
                pos_linha_y = -600  # (caso não seja retorna a posição inicial para em um loop
                                                # para criar a ilusão do movimento do carro seguindo em frente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
        fundo = pygame.image.load('fundo.png')

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_DOWN]:
            y += velocidade
            if y > 480:
                y = 480

        if comandos[pygame.K_UP]:
            y -= velocidade
            if y < 0:
                y = 0
        if comandos[pygame.K_LEFT]:  # a posição não pode ser menor que 196 pois o carro cai na agua a esquerda
            x -= velocidade  #( usar um if)
            if x < 205:
                x = 205

        if comandos[pygame.K_RIGHT]: # a posição não pode ser maior que 526 pois o carro cai na agua a direita
            x += velocidade                 # usar um if se o carro cai na agua perdeu
            if  x > 536:
                x = 536
        if ((x + 55 > pos_policia00x and y +100 >= pos_policia00y and pos_policia00y -150 > 220)):
            x = 369 ; y = 480
        else: pontos += 1

        if (pos_policia00y >  600):
            pos_policia00y = randint(-360, -240)

        if (pos_policia01y >  600):
            pos_policia01y = randint(-620, -500)

        if (pos_ambulanciay > 600):
            pos_ambulanciay = randint(-740, -620)

        if (tempo < 31.25):
            tempo += 1

        else:
            tempo_seg += 1
            texto = fonte.render(" Tempo: "+str(tempo_seg ), True, (255,255,255),(0,0,0))
            tempo =00
            pos_policia00y += vel_carros
            pos_policia01y += vel_carros
            pos_ambulanciay += vel_carros

                                      #retorna o carro da policia a posição inicial
        janela.blit(fundo, (0, 0))
        janela.blit(linhas, (pos_linha_x, pos_linha_y))
        janela.blit(arvore01, (pos_arvore_x1, pos_arvore_y1))
        janela.blit(arvore02, (pos_arvore_x2, pos_arvore_y2))
        janela.blit(arvore03, (pos_arvore_x3, pos_arvore_y3))
        janela.blit(arvore01d, (pos_arvore01dx+2, pos_arvore01dy))
        janela.blit(arvore02d, (pos_arvore02dx+4, pos_arvore02dy))
        janela.blit(arvore03d, (pos_arvore03dx+6, pos_arvore03dy))
        janela.blit(carro10, (x, y))
        janela.blit(policia00, (pos_policia00x , pos_policia00y))
        janela.blit(policia01, (pos_policia01x , pos_policia01y+2))
        janela.blit(ambulancia, (pos_ambulanciax , pos_ambulanciay+1))



        janela.blit(texto, (00, 00))
        pygame.display.update()




pygame.quit()
