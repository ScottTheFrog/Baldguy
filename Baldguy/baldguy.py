import pygame

pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("~Baldguy~ ver 0.0.1")

walkRIGHT = pygame.image.load("player/right_nico_01.png"), pygame.image.load("player/right_nico_02.png")
walkLEFT = pygame.image.load("player/left_nico_01.png"), pygame.image.load("player/left_nico_02.png")
bg = pygame.image.load("background.png")
char = pygame.image.load("player/char.png")
clock = pygame.time.Clock()

x = 100
y = 300
width = 50
height = 50
speed = 10

isJump=False
jumpcount=10
left=False
right=False
walkcount=0

def redrawGameWindow():
    
    global walkcount
    window.blit(bg,(0,0))
    
    if walkcount +1 >=12:
        walkcount = 0
    if left:
        window.blit(walkLEFT[walkcount//6], (x,y))
        walkcount +=1
    elif right:
        window.blit(walkRIGHT[walkcount//6], (x,y))
        walkcount +=1
    else:
        window.blit(char,(x,y))
        
    pygame.display.update()
        
loop = True
while loop:
    clock.tick(60)
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            loop = False
    #movimiento
    key = pygame.key.get_pressed()
     
    if key[pygame.K_LEFT] and x > 0:
        x -=speed
        left=True
        right=False
    elif key[pygame.K_RIGHT] and x <550:
        x+=speed
        left=False
        right=True
    else:
        left=False
        right=False
        walkcount =0
        
    if not isJump:
        if key[pygame.K_SPACE]:
            isJump=True
            left=False
            right=False
            walkcount =0
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount **2) * 0.25 * neg
            jumpcount -=1
        else:
            isJump = False
            jumpcount = 10
            
    redrawGameWindow()
    
pygame.quit()
