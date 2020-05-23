from abc import ABC, abstractmethod

from event import Event


class GameObject(ABC):
    @abstractmethod
    def update(self, event: Event):
        pass

    @abstractmethod
    def render(self):
        pass
