import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuadro Saltando")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Variables de la animación
x, y = 10, height // 2
amplitude = 100  # Amplitud del salto
frequency = 0.05  # Frecuencia del salto
time = 0
is_jumping = False
jump_start_y = height // 2

clock = pygame.time.Clock()

# Función para obtener la posición Y basada en una función seno
def calcular_posicion_y(time):
    return jump_start_y - amplitude * abs(math.sin(frequency * time))

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_jumping:
                is_jumping = True
                time = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and is_jumping:
                is_jumping = False
    
    # Actualizar el tiempo si está saltando
    if is_jumping or y < jump_start_y - 5:
        time += 1

    # Calcular la posición Y del cuadro
    y = calcular_posicion_y(time)

    # Evitar que el cuadro baje de la posición original
    if y > jump_start_y:
        y = jump_start_y

    # Dibujar en la pantalla
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    pygame.display.flip()

    # Controlar la velocidad de la animación
    clock.tick(60)

