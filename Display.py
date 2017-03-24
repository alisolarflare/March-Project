import pygame
class Display:
    def __init__(self, width=800, height=600):
        self.width = width;
        self.height = height;
        self.size = width, height;
        
    def screen(self):
        return pygame.display.set_mode(self.size);