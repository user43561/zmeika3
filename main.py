import pygame
from random import randrange

area = 800 # razreshenie
size = 50

x,y = randrange(0, area, size), randrange(0, area, size)
yabloko = randrange(0, area, size), randrange(0, area, size)
lenght = 1
zmeika = [(x,y)] # определим змейку в виде координат
dx, dy = 0 , 0
V = 5  #скорость змейки

pygame.init() #инициализируем модули pygame
window = pygame.display.set_mode([area,area])
clock = pygame.time.Clock()

while True:
    window.fill(pygame.Color('white')) #white фон
    # нарисуем змейку
    [pygame.draw.rect(window, pygame.Color('black'), (i, j, size - 1, size - 1)) for i, j in zmeika]
    pygame.draw.rect(window, pygame.Color('red'), (*yabloko, size, size))
    #dvizhenie zmeyki
    x += dx * size
    y += dy * size
    zmeika.append((x, y))
    zmeika = zmeika[-lenght:]
    if zmeika[-1] == yabloko:
        yabloko = randrange(size, area - size, size), randrange(size, area - size, size)
        lenght += 1

    pygame.display.flip() # обновляем повернхсотьь
    clock.tick(V)

    for event in pygame.event.get(): # проверка событий на закрытие нашего приложения
        if event.type == pygame.QUIT:
            exit()
    #управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_d]:
        dx, dy = 1, 0