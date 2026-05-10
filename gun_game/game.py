# TODO
# Power Ups - health regen, speed boost, auto reload, damage buff
from Audio import Audio
from pygame import mixer
from Map import Map
from Player import Player
from Gun import Gun
from Bullet import Bullet
from Power_up import Power_up
import pygame
import sys
import copy
import random
import time
def is_collision(position, obstacles):
    is_collision = False    
    for x in obstacles:
        if position.colliderect(x) == True:
            is_collision = True
    return is_collision
pygame.init()
mixer.init()
channel1 = pygame.mixer.Channel(0) 
channel2 = pygame.mixer.Channel(1)  
font = pygame.font.SysFont(None, 25)
font2 =pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
# Create a Map
obstacles = [pygame.Rect(random.randint(80, 150),random.randint(20,200), 10,600), pygame.Rect(random.randint(200,350), random.randint(20,350), 10,450), pygame.Rect(random.randint(400,550),random.randint(20,500), 10,300), pygame.Rect(random.randint(600,750),random.randint(20,350), 10,450), pygame.Rect(random.randint(800,920),random.randint(20,200), 10,600)]
map = Map("map_1", obstacles, [], 1000, 900, (0, 0, 0), (255, 255, 255), 
            [])
screen = pygame.display.set_mode((map.screen_width, map.screen_height))
# Create Weapon
# Assign Weapons
AR = Gun("gun1", 45, 20, 4, 10, 900, 850, 45, {"shot":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\shot2.mp3", 
                                               "reload":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\reload2.mp3"}, 
                                               0, 3)
SMG = Gun("gun2", 50, 20, 5, 5, 500, 500, 50, {"shot":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\smg_sound.mp3", 
                                               "reload":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\reload.mp3"}, 
                                               0, 3)

# Create a Player
player = Player(None, pygame.Rect(950, 400, 50,100), None, 200, "L", 1)
player2 = Player(None, pygame.Rect(0, 400, 50,100), None, 200, "R", 1)
audio= Audio()
player_skin1 = pygame.image.load(r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\Player_skin1.png").convert_alpha()
player_skin1 = pygame.transform.scale(player_skin1, (player.position.width, player.position.height))
left_skin = pygame.transform.flip(player_skin1, True, False)
player_skin2 = pygame.image.load(r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\Player_skin1.png").convert_alpha()
right_skin = pygame.transform.scale(player_skin2, (player2.position.width, player2.position.height))
player.skin = left_skin
player2.skin = right_skin

map1 = pygame.image.load(r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\game_background_1.png").convert_alpha()
map1=pygame.transform.scale(map1, (map.screen_width, map.screen_height))
game_state = "start" # start, end, playing
reveal = False
end_start_time = None
frame = 0
# Game Loop
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:        
            if 445 <= mouse[0] <= 495 and 490 <= mouse[1] <= 540:
                player.weapon = SMG
            elif 525 <= mouse[0] <= 575 and 490 <= mouse[1] <= 540:
                player.weapon = AR
    keys=pygame.key.get_pressed()
    
    if game_state == "start":
        screen.fill((0, 0, 0))
        begin = font2.render(f"Press space to start", True, (255, 255, 255))
        audio.play_audio("lobby", .5)
        screen.blit(begin, (400, 430))
        if keys[pygame.K_SPACE] == True:
            game_state = "guns"
    elif game_state == "guns":
        screen.fill((0, 0, 0))
        choose = font2.render(f"choose your gun. Press v to begin", True, (255, 255, 255))
        choose2 = font2.render(f"for player 2 use buttons 1 and 2 to choose weapons", True, (255, 255, 255))
        screen.blit(choose, (300, 200))          
        button1 = pygame.Rect(445, 490, 50, 50)
        gun_type = font.render(f"SMG", True, (255, 255, 255))
        if 445 <= mouse[0] <= 495 and 490 <= mouse[1] <= 540:
            pygame.draw.rect(screen, (250, 100, 100), button1)
        else:
            pygame.draw.rect(screen, (255, 0, 0), button1)
        
        button2 = pygame.Rect(525, 490, 50, 50)
        gun_type2 = font.render(f"AR", True, (255, 255, 255))
        if 525 <= mouse[0] <= 575 and 490 <= mouse[1] <= 540:
            pygame.draw.rect(screen, (250, 100, 100), button2)
        else:
            pygame.draw.rect(screen, (255, 0, 0), button2)
        if keys[pygame.K_1] == True:
            player2.weapon = copy.deepcopy(SMG)
        elif keys[pygame.K_2] == True:
            player2.weapon = copy.deepcopy(AR)
        if keys[pygame.K_v] == True:
            game_state = "playing"
        screen.blit(gun_type, (447, 505))
        screen.blit(gun_type2, (535, 505))
        screen.blit(choose2, (150, 300))
    elif game_state == "playing":
        player.weapon.power_track()
        player2.weapon.power_track()
        power_up1 = font.render(f"p1 power up: "+ str(player.weapon.powerup), True, (255, 0, 255))
        power_up2 = font.render(f"p2 power up: " + str(player2.weapon.powerup), True,(255, 0, 0))
        audio.play_audio("background", .3)
        #player 1 binds
        new_position = copy.deepcopy(player.position)
        if keys[pygame.K_j] == True and player.position.x > 0:
            new_position.x -= player.speed # update position
            player.update_direction("L")
            player.skin = left_skin
            if is_collision(new_position, map.obstacles) == False:
                player.update_position(-player.speed, 0)
        if keys[pygame.K_l] == True and player.position.x < map.screen_width - player.position.width:
            new_position.x += player.speed 
            player.update_direction("R")
            player.skin = right_skin
            if is_collision(new_position, map.obstacles) == False:
                player.update_position(player.speed, 0)
        if keys[pygame.K_i] == True and player.position.y > 0:
            new_position.y -= player.speed 
            player.update_direction("U")
            if is_collision(new_position, map.obstacles) == False:
                player.update_position(0, -player.speed)
        if keys[pygame.K_k] == True and player.position.y < map.screen_height - player.position.height:
            new_position.y += player.speed 
            player.update_direction("D")
            if is_collision(new_position, map.obstacles) == False:
                player.update_position(0, player.speed)
        if keys [pygame.K_o]:
            player.weapon.reset_reload(480)
            player.weapon.ammo = player.weapon.a_count
            audio.play_sound_effect(player.weapon.sound_effects["reload"], channel1)
        if keys[pygame.K_u]:
            if player.weapon.ammo > 0 and player.weapon.reload == 0:
                if player.weapon.is_ready2_fire() == True:
                    if player.direction == "L":
                        audio.play_sound_effect(player.weapon.sound_effects["shot"], channel2)
                        map.projectiles.append(Bullet(player.weapon.bullet_V, player.direction, pygame.Rect(player.position.x, player.position.y+40, 5, 5), player.weapon.damage, player))
                    elif player.direction == "R":
                        audio.play_sound_effect(player.weapon.sound_effects["shot"], channel2)
                        map.projectiles.append(Bullet(player.weapon.bullet_V, player.direction, pygame.Rect(player.position.x+50, player.position.y+40, 5, 5), player.weapon.damage, player))
                    else:
                        audio.play_sound_effect(player.weapon.sound_effects["shot"], channel2)
                        map.projectiles.append(Bullet(player.weapon.bullet_V, player.direction, pygame.Rect(player.position.x, player.position.y, 5, 5), player.weapon.damage, player))

                    player.weapon.reset_ready2_fire(player.weapon.cooldown)
                    player.weapon.ammo-=1
            
        #player 2 binds
        new_position2 = copy.deepcopy(player2.position)
        if keys[pygame.K_a] == True and player2.position.x > 0:
            new_position2.x -= player2.speed
            player2.update_direction("L")
            player2.skin = left_skin
            if is_collision(new_position2, map.obstacles) == False:
                player2.update_position(-player2.speed, 0)
        if keys[pygame.K_d] == True and player2.position.x < map.screen_width - player2.position.width:
            new_position2.x += player2.speed
            player2.update_direction("R")
            player2.skin = right_skin
            if is_collision(new_position2, map.obstacles) == False:
                player2.update_position(player2.speed, 0)
        if keys[pygame.K_w] == True and player2.position.y > 0:
            new_position2.y -= player2.speed
            player2.update_direction("U")
            if is_collision(new_position2, map.obstacles) == False:
                player2.update_position(0, -player2.speed)
        if keys[pygame.K_s] == True and player2.position.y < map.screen_height - player2.position.height:
            new_position2.y += player2.speed
            player2.update_direction("D")
            if is_collision(new_position2, map.obstacles) == False:
                player2.update_position(0, player2.speed)
        if keys[pygame.K_e]:
            player2.weapon.reset_reload(480)
            player2.weapon.ammo=player2.weapon.a_count
            audio.play_sound_effect(player2.weapon.sound_effects["reload"], channel1)
        if keys[pygame.K_q]:
            if player2.weapon.ammo > 0 and player2.weapon.reload == 0:
                if player2.weapon.is_ready2_fire() == True:
                    if player2.direction == "L":
                        audio.play_sound_effect(player2.weapon.sound_effects["shot"], channel1)
                        map.projectiles.append(Bullet(player2.weapon.bullet_V, player2.direction, pygame.Rect(player2.position.x, player2.position.y+40, 5, 5), player2.weapon.damage, player2))
                    elif player2.direction == "R":
                        audio.play_sound_effect(player2.weapon.sound_effects["shot"], channel1)
                        map.projectiles.append(Bullet(player2.weapon.bullet_V, player2.direction, pygame.Rect(player2.position.x+50, player2.position.y+40, 5, 5), player2.weapon.damage, player2))
                    else:
                        audio.play_sound_effect(player2.weapon.sound_effects["shot"], channel1)
                        map.projectiles.append(Bullet(player2.weapon.bullet_V, player2.direction, pygame.Rect(player2.position.x, player2.position.y, 5, 5), player2.weapon.damage, player2))

                    player2.weapon.reset_ready2_fire(player2.weapon.cooldown)
                    player2.weapon.ammo-=1


        # Update Projectiles
        for bullet in map.projectiles:
            bullet.update_position()
            if bullet.position.colliderect(player.position) and bullet.shot_by == player2:
                map.projectiles.remove(bullet)
                player.decrease_health(bullet.damage)
                print(player.health)
            if bullet.position.colliderect(player2.position) and bullet.shot_by == player:
                map.projectiles.remove(bullet)
                player2.decrease_health(bullet.damage)
                print(player2.health)
            if bullet.position.x > map.screen_width or bullet.position.x < 0:
                map.projectiles.remove(bullet) 
            if bullet.position.y > map.screen_height or bullet.position.y < 0:
                map.projectiles.remove(bullet)
            for obstacle in map.obstacles:
                if bullet.position.colliderect(obstacle):
                    map.projectiles.remove(bullet)
        
        player.weapon.fire_countdown()
        player.weapon.reload_countdown()
        player2.weapon.fire_countdown()
        player2.weapon.reload_countdown()
        # Draw Map
        screen.blit(map1, pygame.Rect(0, 0 , map.screen_width, map.screen_height))
        for i in range(len(map.obstacles)):
            pygame.draw.rect(screen, map.obstacle_color, map.obstacles[i])
        
        
        # randomly spawn power ups
        frame += 1
        if frame >= 2400:
            map.power_ups.append(Power_up(random.randint(1,4), None, pygame.Rect(random.randint(100, 900), random.randint(0, 900), 50, 50)))
            frame = 0
        # draw power ups
        for p in range(len(map.power_ups)-1, -1, -1):
            pygame.draw.rect(screen, map.power_ups[p].color, map.power_ups[p].position)
            if map.power_ups[p].position.colliderect(player.position) == True:
                map.power_ups[p].power_type(player)
                map.power_ups.remove(map.power_ups[p])
            elif map.power_ups[p].position.colliderect(player2.position) == True:
                map.power_ups[p].power_type(player2)
                map.power_ups.remove(map.power_ups[p])

                #lst = [0,1,2] 
                #lne(lst) = 3

        # Draw Player
        screen.blit(player.skin, player.position)
        screen.blit(player2.skin, player2.position)

        # Draw Projectiles
        for b in map.projectiles:
            pygame.draw.rect(screen,(232, 228, 14), b.position)
        screen.blit(power_up1, (835, 50))
        screen.blit(power_up2, (0, 50))
        p1_health = font.render(f"Player 1 health: {player.health}", True, (255, 0, 255))
        screen.blit(p1_health, (835, 0))
        if player.weapon.reload > 0:
            reload1 = font.render(f"Player 1 Reloading...", True, (255, 0, 255))
            screen.blit(reload1,(635,0))
        else:
            ammo1= font.render(f"Player 1 ammo: {player.weapon.ammo}", True, (255, 0, 255))
            screen.blit(ammo1, (635, 0))
        if player2.weapon.reload > 0:
            reload2 = font.render(f"Player 2 Reloading...", True, (255, 0, 0))
            screen.blit(reload2,(200,0))
        else:
            ammo2= font.render(f"Player 2 ammo: {player2.weapon.ammo}", True, (255, 0, 0))
            screen.blit(ammo2, (200, 0))
        p2_health= font.render(f"Player 2 health: {player2.health}", True, (255, 0, 0))
        screen.blit(p2_health, (0, 0))
        if player.health <= 0 or player2.health <= 0:
            game_state = "end"
            audio.play_sound_effect(r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\death.mp3", channel1)
    elif game_state == "end":
        if end_start_time is None:
            end_start_time = pygame.time.get_ticks()
            reveal = False

        # fill bg
        if keys[pygame.K_r] == True:
            player.health, player2.health = 200, 200
            map.projectiles = []
            player.position.x, player2.position.x = 950, 0
            player2.position.y, player.position.y = 400, 400
            player.weapon.ammo, player2.weapon.ammo = 45, 45
            game_state = "start"
            end_start_time = None
        screen.fill((0, 0, 0))
        end = font.render(f"Press r to go to home screen", True, (255, 255, 255))
        result = font.render(f"The winner is... ", True, (255,255,255) )
        audio.play_audio("victory", .5)
        screen.blit(result, (400, 400))
        screen.blit(end, (400, 430))
        
        if end_start_time is not None:
            elapsed = pygame.time.get_ticks() - end_start_time
        else:
            elapsed = 0

        if elapsed >= 5000:
            reveal = True

        if reveal:
            if player2.health <= 0:
                winner = font.render(f"player 1!", True, (255,0,0))
                screen.blit(winner, (530, 400))
            elif player.health <= 0:
                winner2 = font.render(f"player 2!", True, (0, 0,255))
                screen.blit(winner2, (530, 400))
                '''
        if player2.health <= 0:
            if reveal == False:
                time.sleep(3)
            reveal = True
            winner = font.render(f"player 1!", True, (255,0,0) )
            screen.blit(winner, (530, 400))
        if player.health <=0:
            if reveal == False:
                time.sleep(3)
            reveal = True
            winner2 = font.render(f"player 2!", True, (0, 0,255) )
            screen.blit(winner2, (530, 400))
            '''
    
    pygame.display.flip()
    clock.tick(240)


# Takes in player position and list of obstacles, returns True if collision