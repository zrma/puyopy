import copy

from block import Block
from event import Event, RoundEvent
from game_object import GameObject

WIDTH = 13
HEIGHT = 20


class RenderField(GameObject):
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.__height = height
        self.__width = width
        self.__original = [[Block() for _ in range(width)] for _ in range(height)]
        self.__render_target = None

        self.__temp = False

    def update(self, event: Event):
        self.__render_target = copy.deepcopy(self.__original)

        if isinstance(event, RoundEvent):
            self.__temp = not self.__temp

        if self.__temp:
            for line in self.__render_target:
                for block in line:
                    block.set('☆')

    def render(self):
        for line in self.__render_target:
            output = ''
            for block in line:
                output += str(block)

            print(output)

    def set_render_data(self, data, position: tuple):
        assert isinstance(position, tuple)
        x, y = position
        try:
            self.__render_target[self.__height - y - 1][x].set(data)
        except IndexError:
            pass


class LogicField(GameObject):
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.__height = height
        self.__width = width
        self.__original = [[None for _ in range(width)] for _ in range(height)]
        self.__updated = None
        self.__renderer = RenderField(width, height)

    def update(self, event: Event):
        self.renderer.update(event)
        self.__updated = copy.deepcopy(self.__original)

    def set_game_objects(self, game_objects: tuple):
        assert isinstance(game_objects, tuple)

        for game_object in game_objects:
            x, y = game_object.position
            self.__updated[self.__height - y - 1][x] = game_object

    def already_exist(self, position: tuple, game_object: GameObject) -> bool:
        assert isinstance(position, tuple)
        assert isinstance(game_object, GameObject)

        x, y = position
        try:
            return self.__updated[self.__height - y - 1][x] and \
                   self.__updated[self.__height - y - 1][x] != game_object
        except IndexError:
            return False

    def render(self):
        pass

    @property
    def renderer(self):
        return self.__renderer
