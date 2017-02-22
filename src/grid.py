import pygame


class Grid:
    def __init__(self, directory, width, height, column, row, color_key):
        self._grid=pygame.image.load(directory).convert_alpha()
        self._width=width
        self._height=height
        self._column=column
        self._row=row
        if (color_key!="-"):
            self._grid.set_colorkey((int(color_key[2:4],16), int(color_key[4:6],16), int(color_key[6:8],16)),pygame.locals.RLEACCEL)

    def getSpriteRect(self, sprite_id):
        sprite_count=self._column * self._row
        column_width=self._grid.get_rect()[2]/self._column
        row_height=self._grid.get_rect()[3]/self._row
        for row in range(self._row):
            for col in range(self._column):
                if (row*self._column + col == sprite_id):
                    return pygame.Rect(column_width*col, row_height*row, self._width, self._height)

    def renderSprite(self, surface, sprite_id , x, y):
        sprite_rect=self.getSpriteRect(sprite_id)
        grid_rect=self._grid.get_rect()
        grid_rect.centerx+=x
        grid_rect.centery+=y
        surface.blit(self._grid, grid_rect, sprite_rect)
        
        
