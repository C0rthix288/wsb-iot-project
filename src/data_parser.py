from abc import ABC, abstractmethod
from .frame import Frame
from .defined_data import DefinedData

class DataParser(ABC):
    @abstractmethod
    def parse_to_defined_data(self, frame: Frame) -> DefinedData:
        pass

    @abstractmethod
    def parse_to_frame(self, defined_data: DefinedData) -> Frame:
        pass
