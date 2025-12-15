import pygame, random

running = True
menu_active = True
game_active = False
lost_active = False
help_active = False

USER_IMAGE = None
EVENT_IMAGE_A = None
EVENT_IMAGE_B = None
BACKGROUND = None

user_class = None
game_class = None
event_class = None

class Game():
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        self.WIDTH, self.HEIGHT = 896, 640
        self.screen = screen
        self.small_font = pygame.font.Font(None, 64)
        self.smaller_font = pygame.font.Font(None, 46)
        self.background = BACKGROUND
        self.y_1 = 0
        self.y_2 = -self.HEIGHT
        self.scroll_speed = 2

    def update_background(self):
        self.y_1 += self.scroll_speed
        self.y_2 += self.scroll_speed

        if self.y_1 >= self.HEIGHT:
            self.y_1 = -self.HEIGHT
        
        if self.y_2 >= self.HEIGHT:
            self.y_2 = -self.HEIGHT

    def menu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, self.y_1))
        self.screen.blit(self.background, (0, self.y_2))
        self.menu_text = self.small_font.render("Surveillance Skies", True, (0, 0, 0))
        self.menu_prompt = self.smaller_font.render("ENTER to play", True, (0, 0, 0))
        self.help_prompt = self.smaller_font.render("H for help", True, (100, 0, 0))
        self.screen.blit(self.menu_text, ((self.WIDTH - self.menu_text.get_width()) // 2, (self.HEIGHT - self.menu_text.get_height()) // 2 - 15))
        self.screen.blit(self.menu_prompt, ((self.WIDTH - self.menu_prompt.get_width()) // 2, (self.HEIGHT - self.menu_prompt.get_height()) // 2 + 30))
        self.screen.blit(self.help_prompt, ((self.WIDTH - self.help_prompt.get_width()) // 2, (self.HEIGHT - self.menu_text.get_height()) // 2 + 75))
        self.clock.tick(60)
        pygame.display.update()
    
    def game(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, self.y_1))
        self.screen.blit(self.background, (0, self.y_2))
        if not event_class.picked:
            event_class.update()

        user_class.draw()
        event_class.draw()

        self.points_display = self.small_font.render(f"S:{user_class.points}", True, (100, 0, 0))
        self.screen.blit(self.points_display, ((self.WIDTH - self.points_display.get_width()) // 2, (self.HEIGHT - 64)))

        self.clock.tick(60)
        pygame.display.update()

    def game_over(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.text = self.small_font.render("Wrong Move", True, (100, 0, 0))
        self.prompt = self.smaller_font.render("ENTER to return to MENU", True, (0, 0, 0))
        self.screen.blit(self.text, ((self.WIDTH - self.text.get_width()) // 2, (self.HEIGHT - self.text.get_height()) // 2 - 15))
        self.screen.blit(self.prompt, ((self.WIDTH - self.prompt.get_width()) // 2, (self.HEIGHT - self.prompt.get_height()) // 2 + 30))
        self.clock.tick(60)
        pygame.display.update()

    def help(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, self.y_1))
        self.screen.blit(self.background, (0, self.y_2))


        self.main_text = self.small_font.render("Surveillance Skies: HOW TO PLAY?", True, (0, 0, 0))
        self.prompt = self.smaller_font.render("ENTER to return to menu", True, (100, 0, 0))
        self.paragraph_l1 = self.smaller_font.render("You either click [E] to report an enemy (no points)", True, (0, 0, 0))
        self.paragraph_l2 = self.smaller_font.render("or click [F] to fire at an enemy which can earn you points,", True, (0, 0, 0))
        self.paragraph_l3 = self.smaller_font.render("however there is a 1/4 chance of the 'enemy'", True, (0, 0, 0))
        self.paragraph_l4 = self.smaller_font.render("being innocent, making the game over.", True, (0, 0, 0))

        self.screen.blit(self.main_text, ((self.WIDTH - self.main_text.get_width()) // 2, 50))
        self.screen.blit(self.prompt, ((self.WIDTH - self.prompt.get_width()) // 2, 125))
        self.screen.blit(self.paragraph_l1, ((self.WIDTH - self.paragraph_l1.get_width()) // 2, 190))
        self.screen.blit(self.paragraph_l2, ((self.WIDTH - self.paragraph_l2.get_width()) // 2, 240))
        self.screen.blit(self.paragraph_l3, ((self.WIDTH - self.paragraph_l3.get_width()) // 2, 290))
        self.screen.blit(self.paragraph_l4, ((self.WIDTH - self.paragraph_l4.get_width()) // 2, 340))

        self.clock.tick(60)
        pygame.display.update()

class User():
    def __init__(self):
        self.image = USER_IMAGE
        self.report = False
        self.shoot = False
        self.points = 0

    def draw(self):
        if self.image:
            game_class.screen.blit(self.image, ((game_class.WIDTH - 128) // 2, (game_class.HEIGHT - 256) // 2))

class Event():
    def __init__(self):
        self.image_A = EVENT_IMAGE_A
        self.image_B = EVENT_IMAGE_B
        self.image = None
        self.x = 0
        self.y = 10
        self.picked = False
        self.A = False
        self.B = False
        self.dialouges = ["Thermal trace spotted, what do you say?", "Potential enemy on scope?", "Weapons hot or cold?", "Make a decision, ASAP!"]
        self.scroll_speed = 2
        self.last_spawn_time = 0
        self.spawn_delay = 2000
    
    def scroll(self):
        global game_active, lost_active
        if self.picked:
            self.y += self.scroll_speed
            if self.y >= game_class.HEIGHT:
                lost_active = True
                game_active = False

    def random_event(self):
        self.event_choice = random.randint(0, 3)
        if self.event_choice in (0, 1):
            self.A = True
            self.image = self.image_A

        elif self.event_choice in (2,3):
            self.B = True
            self.image = self.image_B

    def random_choice(self):
        global game_active, lost_active
        self.random_choice_int = random.randint(0, 3)
        if self.random_choice_int == 0:
            lost_active = True
            game_active = False

        else:
            if self.picked:
                user_class.points += 1
            self.picked = False

    def update(self):
        current_time = pygame.time.get_ticks()
        if not self.picked and current_time - self.last_spawn_time >= self.spawn_delay:
            self.x = random.randint(0, 896 - 64)
            self.y = 0
            self.dialogue = random.choice(self.dialouges)
            self.image = random.choice([self.image_A, self.image_B])
            self.picked = True
            self.last_spawn_time = current_time

    def draw(self):
        if self.image:
            game_class.screen.blit(self.image, (self.x, self.y))
            self.text = game_class.smaller_font.render(f"{self.dialogue}", True, (0, 0, 0))
            game_class.screen.blit(self.text, ((game_class.WIDTH - self.text.get_width()) // 2, (game_class.HEIGHT - 150)))

def main_loop():
    global running, USER_IMAGE, EVENT_IMAGE_A, EVENT_IMAGE_B, BACKGROUND
    global user_class, game_class, event_class
    global menu_active, game_active, lost_active, help_active

    pygame.init()

    screen = pygame.display.set_mode((896, 640))

    USER_IMAGE = pygame.transform.scale(pygame.image.load("data/user_image.png"), (128, 192))
    EVENT_IMAGE_A = pygame.transform.scale(pygame.image.load("data/event_image_a.png"), (64, 64))
    EVENT_IMAGE_B = pygame.transform.scale(pygame.image.load("data/event_image_b.png"), (64, 64))
    BACKGROUND = pygame.transform.scale(pygame.image.load("data/background.png"), (896, 640))
    
    user_class = User()
    game_class = Game(screen)
    game_class.background = BACKGROUND
    event_class = Event()

    event_class.last_spawn_time = pygame.time.get_ticks( )

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
                    #event_class.y = 0
                    event_class.last_spawn_time = pygame.time.get_ticks()
                    event_class.update()

                if event.key == pygame.K_h and menu_active:
                    game_active = False
                    lost_active = False
                    menu_active = False
                    help_active = True

                if event.key == pygame.K_RETURN and help_active:
                    game_active = False
                    lost_active = False
                    help_active = False
                    menu_active = True

                if event.key == pygame.K_e and game_active:
                    event_class.image = None
                    user_class.shoot = False
                    user_class.report = True
                    event_class.picked = False
                    #event_class.y = 0
                    event_class.last_spawn_time = pygame.time.get_ticks()
                if event.key == pygame.K_f and game_active and event_class.picked:
                    event_class.image = None
                    user_class.report = False
                    user_class.shoot = True
                    event_class.random_choice()
                    #event_class.y = 0
                    event_class.last_spawn_time = pygame.time.get_ticks()
                if event.key == pygame.K_RETURN and not game_active and not menu_active:
                    menu_active = True
                    user_class.points = 0
                    #event_class.y = 0
                
        user_class.report = False
        user_class.shoot = False

        if menu_active:
            game_class.update_background()
            game_class.menu()

        elif game_active:
            game_class.update_background()
            event_class.scroll()
            game_class.game()

        elif lost_active:
            game_class.update_background()
            game_class.game_over()

        elif help_active:
            game_class.update_background()
            game_class.help()

main_loop()

pygame.quit()