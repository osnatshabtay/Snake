import pygame 
class GameOver(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, self.message)


pygame.init()

def display_game_over(screen,width):
    font = pygame.font.SysFont(None, 48)
    text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (width//2 - text.get_width()//2, width//2 - text.get_height()//2))
    pygame.display.update() 