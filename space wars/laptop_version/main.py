
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
bullet_cooldown = 50
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


run = True
lives = 5
wave = 1
enemies = [Enemy(random.randint(10, 450), random.randint(-500, -50), random.choice([en1, en2, en3])), Enemy(random.randint(10, 450), random.randint(-500, -50), random.choice([en1, en2, en3]))]
while run:
	if lives <= 0:
		print('You are Dead!!')
		raise SyntaxError
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				vel_x = 5
			if event.key == pygame.K_LEFT:
				vel_x = -5
			else:
				continue
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				vel_x = 0
	if (pygame.key.get_pressed()[pygame.K_SPACE] and bullet_cooldown <= 0) or (pygame.mouse.get_pressed(3)[2] and bullet_cooldown <= 0):
			bullet_cooldown = 50
			player_bullet_list.append(pygame.Rect(player_rect.x, player_rect.y, 70, 60))
	if pygame.mouse.get_pressed(3)[0]:
		if player_rect.x+30 < pygame.mouse.get_pos()[0]:
			player_rect.x += 5
		elif player_rect.x+30 > pygame.mouse.get_pos()[0]:
			player_rect.x -= 5
		else:
			player_rect.x = pygame.mouse.get_pos()[0] - 30
	if wave == 12:
		print('you Win!!')
		raise SyntaxError
	player_rect.x += vel_x
	if bullet_cooldown > 0:
		bullet_cooldown -= 3
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
			enemies.append(Enemy(random.randint(10, 450), random.randint(-500, -50), random.choice([en1, en2, en3])))
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
	display.blit(player, player_rect)
	display.blit(pygame.font.Font('freesansbold.ttf', 20).render('Lives: {}'.format(str(lives)), True, (255, 255, 255)), (10, 10))
	display.blit(pygame.font.Font('freesansbold.ttf', 20).render('Waves: {}'.format(str(wave)), True, (255, 255, 255)), (10, 40))
	pygame.display.update()
	clock.tick(FPS)
