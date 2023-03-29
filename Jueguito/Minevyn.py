import pygame 
import random
import sys

pygame.init()

#Clases y funciones 
class object_game:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
        
def frame(x):
    return pygame.image.load("Minevyn_textures/{}.png".format(x))

def personaje_juego(x):
    ventana.blit(x, (pos_ini_x, pos_ini_y))

def bloque_juego(x):
    ventana.blit(x, (pos_bloq_x, pos_bloq_y))

#Archivos de Imágenes

fondo_juego = pygame.image.load("Minevyn_textures/fondo1.jpg")
game_over = pygame.image.load("Minevyn_textures/game_over.png")
bloque = pygame.image.load("Minevyn_textures/magma.png")
icono = pygame.image.load("Minevyn_textures/creeper_icon.png")
personaje = pygame.image.load("Minevyn_textures/personaje.png")
pygame.display.set_icon(icono)
pygame.display.set_caption("Minevyn")
pygame.mixer.music.load("Musica/Musica_jueguito.mpeg")
pygame.mixer.music.play(-1)

#Variables de Velocidad

movement = 0
gravity = 0
clock = pygame.time.Clock()

#Ventana

largo = 500
alto = 750
ventana = pygame.display.set_mode((largo,alto))

#Ubicación

pos_ini_x = largo//2 - personaje.get_size()[0]//2
pos_ini_y = alto - personaje.get_size()[1]
l = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
pos_bloq_x = random.choice(l)
pos_bloq_y = -50
block_gravity = 0

#Cuerpo del Juego

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                block_gravity = 7
            if event.key == pygame.K_UP and pos_ini_y >= alto - tamaño2.altura or event.key == pygame.K_SPACE and pos_ini_y >= alto - tamaño2.altura:
                gravity = -10
            if event.key == pygame.K_LEFT:
                movement = -10
            if event.key == pygame.K_RIGHT:
                movement = 10
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                movement = 0

    ventana.blit(fondo_juego, (0,0))
    bloque_juego(bloque)
    pos_bloq_y += block_gravity

    if gravity >= 0 and movement == 0:
        x = personaje
        personaje_juego(x)

    if movement < 0:
        if pos_ini_x <= 0:
            personaje_juego(x)
            x = frame("lado2")
        else:
            x = frame("izq1")
            personaje_juego(x)

    if movement > 0:
        if pos_ini_x >= largo - tamaño1.ancho:
            x = frame("lado1")
            personaje_juego(x)
        else:
            x = frame("der1")
            personaje_juego(x)

    if gravity < 0 and movement == 0:
        x = frame("jump")
        personaje_juego(x)

    if pos_ini_x <= 0:
        pos_ini_x = 0

    tamaño1 = object_game(personaje.get_size()[0], personaje.get_size()[1])
    tamaño2 = object_game(x.get_size()[0], x.get_size()[1])
    pos_ini_y += gravity

    if pos_ini_x >= largo - tamaño1.ancho:
        pos_ini_x = largo - tamaño2.ancho
    pos_ini_x += movement

    if pos_ini_y <= alto - (tamaño1.altura + 140):
        gravity = -gravity

    if pos_ini_y >= alto - tamaño1.altura:
        pos_ini_y = alto - tamaño1.altura

    if pos_bloq_y > alto - bloque.get_size()[1]:
        bloque_juego(bloque)
        pos_bloq_y = 0
        block_gravity += 0.5
        pos_bloq_x = random.choice(l)

    if pos_bloq_x + 50 >= pos_ini_x and pos_bloq_x - 50 <= pos_ini_x and pos_bloq_y + 50 >= pos_ini_y and pos_bloq_y - 50 <= pos_ini_y:
        break

    pygame.display.update() == 0
