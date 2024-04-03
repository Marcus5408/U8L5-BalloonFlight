import pygame


class Balloon:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.image = pygame.image.load(
            f"{__file__.replace('balloon.py', '')}balloon.png"
        )
        self.rescale_image()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5

    def rescale_image(self) -> None:
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.7, self.image_size[1] * 0.7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_balloon(
        self, direction: str, screen_size: tuple, multiplier: int = 1
    ) -> None:
        # move the balloon up or down based on the direction!
        # don't let the balloon move if it's at the bottom or top of the screen
        if direction == "up":
            if self.y > 0:
                self.y = self.y - (self.delta * multiplier)
            else:
                self.y = 0
        else:
            if self.y < screen_size[1] - self.image_size[1]:
                self.y = self.y + (self.delta // 5 * multiplier)
            else:
                self.y = screen_size[1] - self.image_size[1]
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
