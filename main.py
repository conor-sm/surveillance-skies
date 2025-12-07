import pygame, random

pygame.init()

USER_IMAGE = pygame.transform.scale(pygame.image.load("data/user_image.png"), (128, 256))
MENU_IMAGE = pygame.transform.scale(pygame.image.load("data/menu_image.png"), (100, 100))
EVENT_IMAGE_A = pygame.transform.scale(pygame.image.load("data/event_image_a.png"), (64, 64))
EVENT_IMAGE_B = pygame.transform.scale(pygame.image.load("data/event_image_b.png"), (64, 64))

running = True
menu_active = True
game_active = False
lost_active = False

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.WIDTH, self.HEIGHT = 896, 640
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.small_font = pygame.font.SysFont("Aptos", 64)
        self.smaller_font = pygame.font.SysFont("Aptos", 46)

    def menu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(MENU_IMAGE, ((self.WIDTH - 100) // 2, (self.HEIGHT - 100) // 2))
        print(f"menu_active={menu_active} | REPORT={user_class.report} | SHOOT={user_class.shoot} | game_active={game_active} | lost_active={lost_active} | points={user_class.points}")
        self.clock.tick(60)
        pygame.display.update()
    
    def game(self):
        self.screen.fill((0, 0, 0))
        #user_class.update()
        if not event_class.picked:
            event_class.update()

        user_class.draw()
        event_class.draw()

        self.points_display = self.small_font.render(f"S:{user_class.points}", True, (255, 255, 255))
        self.screen.blit(self.points_display, ((self.WIDTH - self.points_display.get_width()) // 2, (self.HEIGHT - 64)))

        print(f"menu_active={menu_active} | REPORT={user_class.report} | SHOOT={user_class.shoot} | game_active={game_active} | lost_active={lost_active} | points={user_class.points}")
        
        self.clock.tick(60)
        pygame.display.update()

    def game_over(self):
        self.screen.fill((0, 0, 0))
        print(f"menu_active={menu_active} | REPORT={user_class.report} | SHOOT={user_class.shoot} | game_active={game_active} | lost_active={lost_active} | points={user_class.points}")
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
        self.image_A = EVENT_IMAGE_A
        self.image_B = EVENT_IMAGE_B
        self.x = 0
        self.y = 10
        self.picked = False
        self.A = False
        self.B = False
        self.dialouges = ["Target acquired in sector 4. Weapons free?", "Bogey on scope. Awaiting fire authorization.", "Hostile inbound! Weapons hot or hold?", "Multiple adults, one child in blast radius. Abort or hold?"]

    def random_event(self):
        self.event_choice = random.randint(0, 1)
        if self.event_choice == 0:
            self.A = True
            self.image = self.image_A

        elif self.event_choice == 1:
            self.B = True
            self.image = self.image_B

    def random_dialouge(self):
        self.dialouge = random.choice(self.dialouges)

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
            self.random_dialouge()
        self.x = self.choice
        self.random_event()

    def draw(self):
        game_class.screen.blit(self.image, (self.x, self.y))
        self.text = game_class.smaller_font.render(f"{self.dialouge}", True, (255, 255, 255))
        game_class.screen.blit(self.text, ((game_class.WIDTH - self.text.get_width()) // 2, (game_class.HEIGHT - 150)))


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