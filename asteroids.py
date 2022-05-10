import pygame, random
import asteroid_generate as ast

pygame.init()

GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SCREENWIDTH = 800
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dodge the Rock!")

ship = ast.Asteroid(50, 50, RED)
ship.rect.x = 350
ship.rect.y = 350

right_rock_1 = ast.Asteroid(50, 1, GREY)
right_rock_1.rect.x = 0
right_rock_1.rect.y = 0
right_rock_2 = ast.Asteroid(50, 1, GREY)
right_rock_2.rect.x = 0
right_rock_2.rect.y = 0
right_rock_3 = ast.Asteroid(50, 1, GREY)
right_rock_3.rect.x = 0
right_rock_3.rect.y = 0

left_rock_1 = ast.Asteroid(50, 1, GREY)
left_rock_1.rect.x = 800
left_rock_1.rect.y = 800
left_rock_2 = ast.Asteroid(50, 1, GREY)
left_rock_2.rect.x = 800
left_rock_2.rect.y = 800
left_rock_3 = ast.Asteroid(50, 1, GREY)
left_rock_3.rect.x = 800
left_rock_3.rect.y = 800

top_rock_1 = ast.Asteroid(50, 1, GREY)
top_rock_1.rect.x = 800
top_rock_1.rect.y = 800
top_rock_2 = ast.Asteroid(50, 1, GREY)
top_rock_2.rect.x = 800
top_rock_2.rect.y = 800
top_rock_3 = ast.Asteroid(50, 1, GREY)
top_rock_3.rect.x = 800
top_rock_3.rect.y = 800

bottom_rock_1 = ast.Asteroid(50, 1, GREY)
bottom_rock_1.rect.x = 0
bottom_rock_1.rect.y = 0
bottom_rock_2 = ast.Asteroid(50, 1, GREY)
bottom_rock_2.rect.x = 0
bottom_rock_2.rect.y = 0
bottom_rock_3 = ast.Asteroid(50, 1, GREY)
bottom_rock_3.rect.x = 0
bottom_rock_3.rect.y = 0

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ship)
all_sprites_list.add(right_rock_1)
all_sprites_list.add(right_rock_2)
all_sprites_list.add(right_rock_3)
all_sprites_list.add(left_rock_1)
all_sprites_list.add(left_rock_2)
all_sprites_list.add(left_rock_3)
all_sprites_list.add(top_rock_1)
all_sprites_list.add(top_rock_2)
all_sprites_list.add(top_rock_3)
all_sprites_list.add(bottom_rock_1)
all_sprites_list.add(bottom_rock_2)
all_sprites_list.add(bottom_rock_3)

right_rocks = pygame.sprite.Group()
right_rocks.add(right_rock_1)
right_rocks.add(right_rock_2)
right_rocks.add(right_rock_3)

left_rocks = pygame.sprite.Group()
left_rocks.add(left_rock_1)
left_rocks.add(left_rock_2)
left_rocks.add(left_rock_3)

top_rocks = pygame.sprite.Group()
top_rocks.add(top_rock_1)
top_rocks.add(top_rock_2)
top_rocks.add(top_rock_3)

bottom_rocks = pygame.sprite.Group()
bottom_rocks.add(bottom_rock_1)
bottom_rocks.add(bottom_rock_2)
bottom_rocks.add(bottom_rock_3)
 
all_rocks = pygame.sprite.Group()
all_rocks.add(right_rocks)
all_rocks.add(left_rocks)
all_rocks.add(top_rocks)
all_rocks.add(bottom_rocks)

carryOn = True
clock = pygame.time.Clock()
 
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.move_left(5)
    if keys[pygame.K_RIGHT]:
        ship.move_right(5)
    if keys[pygame.K_UP]:
        ship.move_up(5)
    if keys[pygame.K_DOWN]:
        ship.move_down(5)
    #Game Logic
        
    for rock in left_rocks:
        rock.move_right(rock.speed)
        if rock.rect.x > SCREENWIDTH:
            rock.respawn(random.randint(25,125), random.randint(3, 8), GREY)
            rock.rect.y = random.randint(0, SCREENHEIGHT)
            rock.rect.x = -100
    for rock in right_rocks:
        rock.move_left(rock.speed)
        if rock.rect.x < 0:
            rock.respawn(random.randint(25,125), random.randint(3, 8), GREY)
            rock.rect.y = random.randint(0, SCREENHEIGHT)
            rock.rect.x = SCREENWIDTH + 100
    for rock in bottom_rocks:
        rock.move_up(rock.speed)
        if rock.rect.y < 0:
            rock.respawn(random.randint(25,125), random.randint(3, 8), GREY)
            rock.rect.x = random.randint(0, SCREENWIDTH)
            rock.rect.y = SCREENHEIGHT + 100
    for rock in top_rocks:
        rock.move_down(rock.speed)
        if rock.rect.y > SCREENHEIGHT:
            rock.respawn(random.randint(25,125), random.randint(3, 8), GREY)
            rock.rect.x = random.randint(0, SCREENWIDTH)
            rock.rect.y = -100
  
    all_sprites_list.update()
    ship_collision_list = pygame.sprite.spritecollide(ship, all_rocks, False)
    for ship in ship_collision_list:
        print("You Died!")
        carryOn=False
    if ship.rect.x > SCREENWIDTH - 49 or ship.rect.x < 0 or ship.rect.y > SCREENHEIGHT - 49 or ship.rect.y < 0:
        print("You Died!")
        carryOn=False
    #Drawing on Screen
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    #Refresh Screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()