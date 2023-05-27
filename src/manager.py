from .data_parser import DataParser
from .listener import Listener
from .my_queue import MyQueue as mQ
from .frame import Frame
from .defined_data import DefinedData

class Manager(DataParser, Listener):
    def __init__(self):
        self.list = mQ()

    def decision(self, frame: Frame):
        pass

    def read_from_db(self, query: str, dd: DefinedData):
        pass

    def read_to_db(self, query: str, dd: DefinedData):
        pass

    # Implement DataParser methods
    def parse_to_defined_data(self, frame: Frame) -> DefinedData:
        pass

    def parse_to_frame(self, defined_data: DefinedData) -> Frame:
        pass

    # Implement Listener methods
    def listen(self, port):
        pass

    def put_to_queue(self, frame: Frame):
        pass
