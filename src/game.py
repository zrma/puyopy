from timer import Timer

from game_object import GameObject
from renderer import Renderer
from event import EventManager

from field import LogicField
import event

from puyo import PuYo


class Game:
    def __init__(self):
        """

        :rtype:
        """
        Timer.init()
        Renderer.init()
        self.__event = EventManager()
        self.__game_objects = {}
        self.__field = LogicField()

        self.__current_pu_yo: PuYo = None

    def run(self):

        is_continue = True
        while is_continue:
            is_continue = self.__update()
            self.__render()

    def __update(self) -> bool:
        Timer.capture_time()

        current_event = self.__event.get_event()
        if isinstance(current_event, event.GameExitEvent):
            return False

        self.__field.update(current_event)
        self.__field.set_game_objects(tuple(self.__game_objects.values()))

        for game_object in self.__game_objects.values():
            assert isinstance(game_object, GameObject)
            game_object.update(current_event)

        current_pu_yo = self.__current_pu_yo
        if not current_pu_yo or not current_pu_yo.valid:
            new_pu_yo = PuYo(self.__field)
            self.__current_pu_yo = new_pu_yo
            self.__game_objects[new_pu_yo.id] = new_pu_yo

        return True

    def __render(self):
        if not Renderer.render_begin(self.__field.renderer):
            return

        for game_object in self.__game_objects.values():
            assert isinstance(game_object, GameObject)
            game_object.render()

        Renderer.render_end()
