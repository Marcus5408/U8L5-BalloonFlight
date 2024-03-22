import pygame


class Balloon:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("balloon.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_balloon(self, direction):
        # move the balloon up or down based on the direction!
        # don't let the balloon move if it's at the bottom or top of the screen
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


