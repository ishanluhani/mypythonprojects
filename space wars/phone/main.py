import pygame
import random

pygame.font.init()
pygame.mixer.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Space Wars')
background = pygame.transform.scale(pygame.image.load('assets/background-black.png'), (500, 500))
clock = pygame.time.Clock()
FPS = 60
player = pygame.transform.scale(pygame.image.load('assets/pixel_ship_yellow.png'), (70, 60))
bullet = pygame.transform.scale(pygame.image.load('assets/pixel_laser_yellow.png'), (70, 60))

en1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/pixel_ship_blue_small.png'), (70, 60)), False, True)
bl1 = pygame.transform.scale(pygame.image.load('assets/pixel_laser_blue.png'), (70, 60))
en2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/pixel_ship_green_small.png'), (70, 60)), False, True)
bl2 = pygame.transform.scale(pygame.image.load('assets/pixel_laser_green.png'), (70, 60))
en3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/pixel_ship_red_small.png'), (70, 60)), False, True)
bl3 = pygame.transform.scale(pygame.image.load('assets/pixel_laser_red.png'), (70, 60))

player_rect = player.get_rect()
player_rect.x = 215
player_rect.y = 400
music = pygame.mixer.music.load('space_invader (mp3cut.net) (1).mp3')
pygame.mixer.music.play(999999999)
player_bullet_list = []
waves = 2
bullet_cooldown = 100
vel_x = 0


class Enemy():
	def __init__(self, x, y, color):
		self.image = color
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def draw(self):
		display.blit(self.image, self.rect)

	def move(self, vel):
		self.rect.y += 1
def text_(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()
def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(display, ac,(x,y,w,h))

        if click[0] == 1:
            return True
        else:
        	return False
    else:
        pygame.draw.rect(display, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)
run = True
lives = 5
wave = 1
enemies = [Enemy(random.randint(10, 450), random.randint(-1000, -50), random.choice([en1, en2, en3])), Enemy(random.randint(10, 450), random.randint(-1000, -50), random.choice([en1, en2, en3]))]
while run:
	if lives <= 0:
		print('You are Dead!!')
		print('bye!!')
		break
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	if wave == 12:
		print('you Win!!')
		print('bye!!')
		break
	player_rect.x += vel_x
	if bullet_cooldown > 0:
		bullet_cooldown -= 2
	if player_rect.x + player_rect.w >= 500:
		player_rect.x = 500 - player_rect.w
	elif player_rect.x <= 0:
		player_rect.x = 0
	display.blit(background, (0, 0))
	for bullets in player_bullet_list:
		if bullets.y < 0:
			player_bullet_list.remove(bullets)
		bullets.y -= 10
		display.blit(bullet, bullets)
	if len(enemies) == 0:
		waves += 3
		wave += 1
		for i in range(waves):
			enemies.append(Enemy(random.randint(10, 450), random.randint(-1000, -50), random.choice([en1, en2, en3])))
	left = button('<=', 10, 440, 50, 50, (0, 200, 0), (0, 255, 0))
	right = button('=>', 440, 440, 50, 50, (0, 200, 0), (0, 255, 0))
	shoot = button('shoot', 225, 460, 50, 30, (0, 0, 200), (0, 0, 255))
	if left:
		button('<=', 10, 440, 50, 50, (0, 244, 0), (0, 255, 0))
		vel_x = -5
	elif right:
		button('=>', 440, 440, 50, 50, (0, 244, 0), (0, 255, 0))
		vel_x = 5
	else:
		vel_x = 0
	if shoot and bullet_cooldown <= 0:
		bullet_cooldown = 100
		player_bullet_list.append(pygame.Rect(player_rect.x, player_rect.y, 70, 60))
	for enemy in enemies[:]:
		enemy.move(1)
		enemy.draw()
		for i in player_bullet_list:
			if enemy.rect.colliderect(i) and enemy.rect.y > 20:
				enemies.remove(enemy)
				player_bullet_list.remove(i)
		if enemy.rect.y >= 500:
			lives -= 1
			enemies.remove(enemy)
	if bullet_cooldown > 0:
		bullet_cooldown -= 3
	display.blit(player, player_rect)
	display.blit(pygame.font.Font('freesansbold.ttf', 20).render('Lives: {}'.format(str(lives)), True, (255, 255, 255)), (10, 10))
	display.blit(pygame.font.Font('freesansbold.ttf', 20).render('Waves: {}'.format(str(wave)), True, (255, 255, 255)), (10, 40))
	pygame.display.update()
	clock.tick(FPS)