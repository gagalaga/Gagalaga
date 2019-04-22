import pygame
import os

from src.Config import color_configs as colors

from src.Drawable import Drawable
from src.Collideable import Collideable


class Shot(Drawable, Collideable):
    """
    A class that encapsulates the logic behind of a shot.
    Being it from an user or an enemy.
    """

    def __init__(self, current_position, current_velocity, screen):
        Drawable.__init__(self, current_position, ((3/2)*current_velocity[0], (3/2)*current_velocity[1]) , screen, (5,10))
        self._shotImage = pygame.image.load(os.path.abspath("static/Images/Player/player-gun.png"))
        self._shotImage = pygame.transform.scale(self._shotImage, self._size)
        self._shotImage = self._shotImage.convert_alpha()

        pygame.mixer.init()
        shot_sound = pygame.mixer.Sound('./static/sounds/shoot1.wav')
        shot_sound.set_volume(1)
        shot_sound.play()

        Collideable.__init__(self)

    def draw(self):
        self._screen.blit(self._shotImage, self._position)

    @property
    def image(self):
        return self._shotImage

    @property
    def position(self):
        return self._position
