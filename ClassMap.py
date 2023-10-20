import pygame
import pygame.gfxdraw
from Buttons import AddUnitButton
from Buttons import AddUnitStringButton
from Unit import Unit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PIC_WIDTH = 768
PIC_HEIGHT = 537
BLOCK_SIZE = 35

class Map:
    def __init__(self):
        pygame.init()
        self.is_work_ = True
        self.clock_ = pygame.time.Clock()
        self.fps_ = 30
        self.width_ = 1000
        self.height_ = 537
        self.window_ = pygame.display.set_mode((self.width_, self.height_), pygame.SCALED)
        self.creat_background()
        self.draw_grid()

    def draw_grid(self):
        for x in range(0, PIC_WIDTH, BLOCK_SIZE):
            for y in range(0, PIC_HEIGHT, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.window_, BLACK, rect, 1)

    def creat_background(self):
        self.window_.fill(WHITE)
        bg_surf_ = pygame.image.load("map_pic.PNG").convert()
        self.window_.blit(bg_surf_, [0, 0])

    def add_unit(self, x, y, date, time):
        unit = Unit(x, y, date, time, self.window_)
        unit.draw_unit()

    # def draw_add_unit_button(self):
    #     button = AddUnitButton(self.window_, 775, 0)
    #     button.draw_button()

    def run_game(self):
        frodo = Unit(215, 313, "12.10.2004", "12:03", self.window_)
        frodo.draw_unit()
        button = AddUnitButton(self.window_, 775, 0)
        button.draw_button()
        box = AddUnitStringButton(self.window_, 825, 0)
        text = ''
        while self.is_work_:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_work_ = False
                    break
                if button.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and button.is_pressed_:
                    box.draw_button()
                    button.is_pressed_ = False
                    if box.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and box.is_active_:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                text.split(' - ')
                                date = text[0]
                                time = text[1]
                                coordinates = text[3][1:-2].split(',')
                                x = int(coordinates[0])
                                y = int(coordinates[1][1::])
                                unit = Unit(self.window_, x, y, date, time)
                                unit.draw_unit()
                                text = ''
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode
                    if box.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 0 and not box.is_active_:
                        box.is_active_ = False
                if button.target_.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 0 and not button.is_pressed_:
                    button.is_pressed_ = True

            self.clock_.tick(self.fps_)
            pygame.display.update()
        # self.clock_.tick(self.fps_)