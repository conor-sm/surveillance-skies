import pygame, random

pygame.init()

USER_IMAGE = pygame.transform.scale(pygame.image.load("data/user_image.png"), (128, 256))
MENU_IMAGE = pygame.transform.scale(pygame.image.load("data/menu_image.png"), (100, 100))
EVENT_IMAGE = pygame.transform.scale(pygame.image.load("data/event_image.png"), (64, 64))

running = True
menu_active = True
game_active = False
lost_active = False

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.WIDTH, self.HEIGHT = 896, 640
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def menu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(MENU_IMAGE, ((self.WIDTH - 100) // 2, (self.HEIGHT - 100) // 2))
        print("Hello World: MENU")
        self.clock.tick(60)
        pygame.display.update()
    
    def game(self):
        self.screen.fill((0, 0, 0))
        #user_class.update()
        if not event_class.picked:
            event_class.update()
        user_class.draw()
        event_class.draw()
        print(f"GAME: REPORT={user_class.report} | SHOOT={user_class.shoot}")
        self.clock.tick(60)
        pygame.display.update()

    def game_over(self):
        self.screen.fill((0, 0, 0))
        print(f"OVER: REPORT={user_class.report} | SHOOT={user_class.shoot}")
        self.clock.tick(60)
        pygame.display.update()

class User():
    def __init__(self):
        self.image = USER_IMAGE
        self.report = False
        self.shoot = False
        self.points = 0

    #def update(self):

    def draw(self):
        game_class.screen.blit(self.image, ((game_class.WIDTH - 128) // 2, (game_class.HEIGHT - 256) // 2))

class Event():
    def __init__(self):
        self.image = EVENT_IMAGE
        self.x = 0
        self.y = 10
        self.picked = False

    def random_x(self):
        self.choice = random.randint(0, (896 - 64))
        self.picked = True

    def random_choice(self):
        global game_active, lost_active
        self.random_choice_int = random.randint(0, 1)
        if self.random_choice_int == 0:
            lost_active = True
            game_active = False

        elif self.random_choice_int == 1:
            user_class.points += 1
            self.picked = False

    def update(self):
        if not self.picked:
            self.random_x()
        self.x = self.choice

    def draw(self):
        game_class.screen.blit(self.image, (self.x, self.y))


user_class = User()
game_class = Game()
event_class = Event()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and menu_active:
                game_active = True
                menu_active = False
                user_class.points = 0
                event_class.picked = False
            if event.key == pygame.K_e and game_active:
                user_class.shoot = False
                user_class.report = True
                event_class.picked = False
            if event.key == pygame.K_f and game_active:
                user_class.report = False
                user_class.shoot = True
                event_class.random_choice()
            if event.key == pygame.K_RETURN and not game_active and not menu_active:
                menu_active = True
                user_class.points = 0
            
    user_class.report = False
    user_class.shoot = False

    if menu_active:
        game_class.menu()

    elif game_active:
        game_class.game()

    elif lost_active:
        game_class.game_over()

pygame.quit()