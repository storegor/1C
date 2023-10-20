import pygame.gfxdraw

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class AddUnitButton:
    def __init__(self, screen, x, y):
        self.surf_ = pygame.Surface((35, 35))
        self.colour_ = BLACK
        self.is_pressed_ = False
        self.place_ = (x, y)
        self.click_zone_ = (x + 15, y + 15)
        self.screen_ = screen
        self.target_ = self.surf_.get_rect(centerx=self.click_zone_[0], centery=self.click_zone_[1])

    def draw_button(self):
        self.screen_.blit(self.surf_, self.place_)
        plus_pic = pygame.font.SysFont('arial', 50).render(str("+"), False, WHITE, None)
        self.screen_.blit(plus_pic, (self.place_[0] + 3, self.place_[1] - 12))

class AddUnitStringButton:
    def __init__(self, screen, x, y):
        self.colour_ = BLACK
        self.is_active_ = False
        self.place_ = (x, y)
        self.click_zone_ = (x + 15, y + 15)
        self.screen_ = screen
        self.surf_ = pygame.Surface((150, 35))
        self.target_ = self.surf_.get_rect(centerx=self.click_zone_[0], centery=self.click_zone_[1])

    def draw_button(self):
        self.screen_.blit(self.surf_, self.place_)