import pygame
from pygame.locals import *
import math


class RadioButton:
    def __init__(self, size, color, choices, x_distance, y_distance):
        self._size=size
        self._choices=choices
        self._x_distance=x_distance
        self._y_distance=y_distance
        self._color=color
        self._current_choice=0
        self._position_x=0
        self._position_y=0

    def renderButtons( self, surface, x, y ):
        self._position_x=x
        self._position_y=y
        for button_count in range(self._choices):
            pygame.draw.circle(surface, self._color, (x+(self._x_distance*button_count), y+(self._y_distance*button_count)), self._size, 2)
            if (button_count==self._current_choice):
                if (self._size-3 > 0):
                    highlight_size=self._size-3
                else:
                    highlight_size=1
                pygame.draw.circle(surface, (255,0,0), (x+(self._x_distance*button_count), y+(self._y_distance*button_count)), highlight_size,4)

    def checkButtonClicked( self, mouse_position ):
        for button_count in range(self._choices):
            if (math.sqrt((mouse_position[0]-(self._position_x+self._x_distance*button_count))**2 + (mouse_position[1]-(self._position_y+self._y_distance*button_count))**2) <= self._size):
                self._current_choice=button_count
                return str(button_count) 
        return False
        
