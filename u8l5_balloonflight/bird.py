import pygame


class Bird:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        image_dir = __file__.replace("bird.py", "")
        self.image_list = [f"{image_dir}bird-up.png", f"{image_dir}bird-down.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5
        self.up = True

    def rescale_image(self):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.7, self.image_size[1] * 0.7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_bird(self):
        self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def switch_image(self):
        image_number = 0
        if not self.up:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image()
        self.image_size = self.image.get_size()
        self.up = not self.up
