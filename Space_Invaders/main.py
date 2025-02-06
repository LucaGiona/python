import pygame
import  random
import math

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spaceship = Spaceship(self, 370, 515)
        self.score = 0

        self.enemies = []
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(20, 50)))# breite des Alien Bildes

        self.background_img= pygame.image.load("spr_space_himmel-1.png")


        #the gameloop
        while self.running:
            self.clock.tick(60)
            #self.screen.fill((233,154,22)) #Farbe Hintergrund ändern
            self.screen.blit(self.background_img, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-5)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(5)
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(5)# hier wird der Wert wieder auf null gesetzt
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-5)
            self.spaceship.update()
            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired == True:
                        bullet.update()
                    else:
                        self.spaceship.bullets.remove(bullet)

            for enemy in self.enemies:
                enemy.update()
                enemy.check_collision()
                if enemy.y > 460:
                    for i in self.enemies:
                        i.y = 1000. # enemies ewrden so platziert, dass sie nicht mehr sichtbar sind
                    #Game over text
                    self.print_game_over()
                    break

            self.print_score()
            pygame.display.update()


    def print_game_over(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)
        #text muss gerendert werden
        go_text = go_font.render("GAME OVER", True, (255,255,255))
        self.screen.blit(go_text, (200,250))

    def print_score(self):
        score_font = pygame.font.Font("freesansbold.ttf", 19)
        score_text = score_font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (8, 8))


class Spaceship:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.game = game
        self.spaceship_img = pygame.image.load("spr_spaceship-1.png")
        self.bullets = []

    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))
        self.bullets[len(self.bullets) -1].fire()

    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x += self.change_x
        if self.x < 0:
            self.x = 0
        elif self.x > 736:# breite des Spaceship Bildes muss noch abgezogen werden
            self.x = 736
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))

class Bullet:
    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.game = game
        self.is_fired = False
        self.bullet_speed = 10
        self.bullet_img = pygame.image.load("spr_patrone.png")

    def fire(self):
        self.is_fired = True

    def update(self):
        self.y -= self.bullet_speed
        if self.y <= 0:
            self.is_fired = False
        self.game.screen.blit(self.bullet_img, (self.x, self.y))

class Enemy:
    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.change_x = 5
        self.change_y = 60
        self.game = game
        self.enemy_img = pygame.image.load("spr_space_enemy.png")

    def check_collision(self):
        for bullet in self.game.spaceship.bullets:
            distance = math.sqrt(math.pow(self.x - bullet.x, 2) + math.pow(self.y - bullet.y, 2))
            if distance < 35:
                bullet.is_fired = False
                self.game.score += 1
                self.x = random.randint(0, 736)
                self.y = random.randint(50, 150)


    def update(self):
        self.x += self.change_x
        if self.x >= 736:
            self.y += self.change_y
            self.change_x = -5
        elif self.x <= 0:
            self.y += self.change_y
            self.change_x = 5
        self.game.screen.blit(self.enemy_img, (self.x, self.y))

if __name__ == "__main__":
    game = Game(800, 580)
    print(len(game.spaceship.bullets))