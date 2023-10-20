import pygame.gfxdraw
import random
RADIUS = 10
BLOCK_SIZE = 35
class Unit:
    def __init__(self, x, y, date, time, screen):
        self.color_ = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.uploading_date_ = date
        self.uploading_time_ = time
        self.location_ = (x - x % BLOCK_SIZE, y - y % BLOCK_SIZE)
        self.screen_ = screen
        pygame.gfxdraw.filled_circle(self.screen_, self.location_[0], self.location_[1], RADIUS, self.color_)

    def draw_unit(self):
        pygame.gfxdraw.filled_circle(self.screen_, self.location_[0], self.location_[1], RADIUS, self.color_)
