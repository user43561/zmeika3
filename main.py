import pygame
from random import randrange

area = 900 # razreshenie
size = 20

x,y = randrange(0, area, size), randrange(0, area, size)
yabloko = randrange(0, area, size), randrange(0, area, size)
lenght = 1
score = 0
zmeika = [(x,y)] # определим змейку в виде координат
dx, dy = 0 , 0
V = 10  #скорость змейки
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }

pygame.init() #инициализируем модули pygame
window = pygame.display.set_mode([area,area])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Gothic', 26, bold = True )

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
    #счет
    displayscore = font_score.render(f'SCORE: {score}', 1, pygame.Color('black'))
    window.blit(displayscore, (5,5))
    if zmeika[-1] == yabloko:
        yabloko = randrange(size, area - size, size), randrange(size, area - size, size)
        lenght += 1
        score += 1
    #варианты проигрыша
    if x < 0 or x > area + size or y < 0 or y > area-size:
        break
    if len(zmeika) != len(set(zmeika)):
        break


    pygame.display.flip() # обновляем повернхсотьь
    clock.tick(V)

    for event in pygame.event.get(): # проверка событий на закрытие нашего приложения
        if event.type == pygame.QUIT:
            exit()
    #управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
