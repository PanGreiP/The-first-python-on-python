import pygame
import random

width = 550
length = 550
resolution = [length, width]
done = 0
grid_color = [0,0,0]
grid_thickness = 5
borders_distantion = 10
cubes_in_width = width // 20
cubes_in_length = length // 20

window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Heya fucker")
screen = pygame.Surface(resolution)

class Player():
    def __init__(self, xpos, ypos, filename):
        self.xpos = xpos
        self.ypos = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.xpos * 20,self.ypos * 20))


def tail_going():
    x = 2
    y = len(list)
    for i in reversed(list[1:]):
            i.xpos, i.ypos = list[y - x].xpos, list[y - x].ypos
            x += 1

counter = 0 #для будущего счёта
tail = Player(4, 5, 'element.png')
hero = Player(4, 4, 'element.png')
going = '' # для клавиш
list = [hero, tail]
def do_going(going):
    if going == 'left':
        tail_going()
        list[0].xpos -= 1
        if list[0].xpos < 0:
            list[0].xpos = length // 20
    if going == 'right':
        tail_going()
        list[0].xpos += 1
        if list[0].xpos > length // 20:
            list[0].xpos = 0
    if going == 'up':
        tail_going()
        list[0].ypos -= 1
        if list[0].ypos < 0:
            list[0].ypos = width // 20
    if going == 'down':
        tail_going()
        list[0].ypos += 1
        if list[0].ypos > width // 20:
            list[0].ypos = 0

apple = Player(10, 10, 'apple.png')
def apple_gen(list):
    x = random.randint(0, cubes_in_length)
    y = random.randint(0, cubes_in_width)
    for i in list:
        if (i.xpos, i.ypos) == (x, y):
            x, y = apple_gen(list)
        else:
            continue
    return x, y
apple.xpos, apple.ypos = apple_gen(list)

def grid_draw():
    x = length
    x0 = 0
    y = width
    y0 = 0
    while x0<length:
        pygame.draw.line(screen, (grid_color), (x0, y0), (x0, y), 1)
        x0 += borders_distantion
    x0 = 0
    while y0<width:
        pygame.draw.line(screen, (grid_color), (x0, y0), (x, y0), 1)
        y0 += borders_distantion
    y0 = 0
    pygame.draw.line(screen, (grid_color), (x0, y), (x, y), grid_thickness)
    pygame.draw.line(screen, (grid_color), (x, y), (x, y0), grid_thickness)
    pygame.draw.line(screen, (grid_color), (x0, y0), (x0, y), grid_thickness)
    pygame.draw.line(screen, (grid_color), (x0, y0), (x, y0), grid_thickness)

pygame.init()
while not done:
    some_x = list[len(list) - 1].xpos
    some_y = list[len(list) - 1].ypos
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                going = 'left'
            if event.key == pygame.K_RIGHT:
                going = 'right'
            if event.key == pygame.K_UP:
                going = 'up'
            if event.key == pygame.K_DOWN:
                going = 'down'


    do_going(going)
    if list[0].xpos == apple.xpos and list[0].ypos == apple.ypos:
        counter += 1
        list.append(Player(some_x, some_y, 'element.png'))
        apple.xpos, apple.ypos = apple_gen(list)


    screen.fill((135, 82, 201))
    grid_draw()
    font = pygame.font.Font("2204.ttf", 25)
    score = font.render("Score: " + str(counter), True, (0,0,0))
    screen.blit(score, [0,0])
    if counter < 10:
        pygame.draw.rect(screen, (0,0,0), ([0,0], [100,31]), 2)
    elif counter < 100:
        pygame.draw.rect(screen, (0,0,0), ([0,0],[110,31]), 2)
    for i in list:
        i.render()
    apple.render()

#   print(apple.xpos, apple.ypos,'|', hero.xpos,hero.ypos)

    grid_draw()
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(100)

