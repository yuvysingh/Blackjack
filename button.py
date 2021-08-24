import pygame

pygame.init()
gui_font = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
MAGENTA_PINK = (94, 60, 82)
RED = (97, 57, 64)


class Button:
    def __init__(self, text, pos, width, height):

        # Button rectangle
        self.rect = pygame.Rect(pos, (width, height))
        self.color = MAGENTA_PINK

        # Text
        self.text_surf = gui_font.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

        self.clicked = False

    def draw(self, screen):

        # Draw the button on the screen
        pygame.draw.rect(screen, self.color, self.rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self):

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):

            self.color = RED

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

                return self.clicked

            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                return self.clicked

        else:
            self.color = MAGENTA_PINK

    def score_update(self, new_text):

        self.text_surf = gui_font.render(new_text, True, WHITE)
