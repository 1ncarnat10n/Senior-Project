import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Kingdom Come')
        pygame_icon = pygame.image.load('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/graphics/test/player.png')
        pygame.display.set_icon(pygame_icon)
        self.clock = pygame.time.Clock()

        self.level = Level()

        main_sound = pygame.mixer.Sound('/Users/basedatlas/Desktop/SeniorProject/Senior-Project/audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

