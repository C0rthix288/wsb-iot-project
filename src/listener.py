from abc import ABC, abstractmethod
from .frame import Frame

class Listener(ABC):
    @abstractmethod
    def listen(self, port):
        pass

    @abstractmethod
    def put_to_queue(self, frame: Frame):
        pass
