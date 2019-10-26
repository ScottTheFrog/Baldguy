import pygame
import time

pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("~Baldguy~ ver 0.0.2")
walkRIGHT = pygame.image.load("player/right_nico_01.png"), pygame.image.load("player/right_nico_02.png")
walkLEFT = pygame.image.load("player/left_nico_01.png"), pygame.image.load("player/left_nico_02.png")
bg = pygame.image.load("background.png")
char = pygame.image.load("player/char.png")
baldguy = pygame.image.load("baldguy.png")
clock = pygame.time.Clock()

class baldguy():
    def __init__(self, x,y,width,height):
        self.x =x
        self.y =y
        self.width = width
        self.height=height
        self.speed = 10
        self.isJump = False
        self.jumpcount =10
        self.left = False
        self.right=False
        self.walkcount=0

    def sprite(self,window):
        if self.walkcount +1 >=12:
            self.walkcount = 0
        if self.left:
            window.blit(walkLEFT[self.walkcount//6], (self.x,self.y))
            self.walkcount +=1
        elif self.right:
            window.blit(walkRIGHT[self.walkcount//6], (self.x,self.y))
            self.walkcount +=1
        else:
            window.blit(char,(self.x,self.y))
def redrawGameWindow():
    window.blit(bg,(0,0))
    baldguy.sprite(player,window)
    pygame.display.update()

    
player = baldguy(300,300,50,50)        
loop = True
while loop:
    clock.tick(60)
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            loop = False
    key = pygame.key.get_pressed()
     
    if key[pygame.K_LEFT] and player.x > 0:
        player.x -=player.speed
        player.left=True
        player.right=False
    elif key[pygame.K_RIGHT] and player.x <550:
        player.x+=player.speed
        player.left=False
        player.right=True
    else:
        player.left=False
        player.right=False
        player.walkcount =0
        
    if not (player.isJump):
        if key[pygame.K_SPACE]:
            player.isJump=True
            player.left=False
            player.right=False
            player.walkcount =0
            player.speed=5
    else:
        if player.jumpcount >= -10:
            neg = 1
            if player.jumpcount < 0:
                neg = -1
            player.y -= (player.jumpcount **2) * 0.25 * neg
            player.jumpcount -=1
        else:
            player.isJump = False
            player.jumpcount = 10
            player.speed=10
    redrawGameWindow()
    
pygame.quit()
