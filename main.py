import pygame

pygame.init()

USER_IMAGE = pygame.transform.scale(pygame.image.load("data/user_image.png"), (128, 256))
MENU_IMAGE = pygame.transform.scale(pygame.image.load("data/menu_image.png"), (100, 100))

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
        self.screen.blit(USER_IMAGE, ((self. WIDTH - 128) // 2, (self.HEIGHT - 256) // 2))
        print("Hello World: GAME")
        self.clock.tick(60)
        pygame.display.update()

game_class = Game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and menu_active:
                game_active = True
                menu_active = False


    if menu_active:
        game_class.menu()

    elif game_active:
        game_class.game()

pygame.quit()