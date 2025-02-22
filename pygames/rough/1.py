
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
player=pygame.Rect((280,250,50,50))
speed= 1
player1=pygame.Rect((0,100,50,50))
player2=pygame.Rect((200,0,50,50))
player3=pygame.Rect((0,0,50,50))

run = True
while run:
    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(0,255,0),player1)
    pygame.draw.rect(screen,(0,0,255),player2)
    pygame.draw.rect(screen,(50,100,255),player3)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player.move_ip(-1, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player.move_ip(1, 0)
    if key[pygame.K_UP] or key[pygame.K_w]:
        player.move_ip(0, -1)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        player.move_ip(0, 1)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
