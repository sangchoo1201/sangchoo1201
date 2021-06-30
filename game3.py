import pygame
import random

# 환경 설정
clock = pygame.time.Clock()
fps = 200

screen_width = 1000
screen_height = 1000
tile_size = 20

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.init()

pygame.display.set_caption("Nano Platformer")

# 이미지 선언
bg_img = pygame.image.load("img/bg.png")


class Button:
    def __init__(self, x, y):
        img = pygame.image.load("img/spike.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed(3)[0] == 1 and not self.clicked:
            action = True
            self.clicked = True
        elif pygame.mouse.get_pressed(3)[0] == 1 and not self.clicked:
            self.clicked = True
        if pygame.mouse.get_pressed(3)[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)
        return action


class Mouse:
    def __init__(self):
        pos = pygame.mouse.get_pos()
        self.image = pygame.image.load("img/mouse.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]-1
        self.rect.y = pos[1]-1
        self.counter = 0

    def draw(self):
        self.counter += 1
        screen.blit(self.image, self.rect)


x_pos = 490
y_pos = 490
button = Button(x_pos, y_pos)
mouse_list = []

# 게임 구동
run = True
while run:

    clock.tick(fps)

    screen.blit(bg_img, (0, 0))
    mouse_list.append(Mouse())
    for i in mouse_list:
        if i.counter > 50:
            del i
        else:
            i.draw()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        run = False

    if button.draw(x_pos, y_pos):
        x_pos = random.randint(0, 1000-tile_size)
        y_pos = random.randint(0, 1000-tile_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
