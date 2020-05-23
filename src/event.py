from abc import ABC

from pynput.keyboard import Key, Listener


class Event(ABC):
    pass


class VoidEvent(Event):
    pass


class GameExitEvent(Event):
    pass


class MoveLeftEvent(Event):
    pass


class MoveRightEvent(Event):
    pass


class RoundEvent(Event):
    pass


class FallEvent(Event):
    pass


class EventManager:
    def __init__(self):
        self.__listener = Listener(on_release=__class__.on_release)
        self.__listener.start()

    @staticmethod
    def on_release(key):
        __class__.__current_key = key
        # print('{0} pressed'.format(__class__.__current_key))

    @staticmethod
    def get_event() -> Event:
        handlers = {
            Key.esc: GameExitEvent,
            Key.left: MoveLeftEvent,
            Key.right: MoveRightEvent,
            Key.space: RoundEvent
        }

        try:
            current_key = __class__.__current_key
            __class__.__current_key = None
            return handlers[current_key]()
        except KeyError:
            return VoidEvent()

    __current_key = None
