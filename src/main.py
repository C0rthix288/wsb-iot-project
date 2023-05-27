from .manager import Manager
from .listener import Listener
from .data_parser import DataParser
from .db_manager import DBManager
from .kafka_manager import KafkaManager
from manager_config import db_config, kafka_config

def main():
    # Create instances of your classes
    db_manager = DBManager(db_config)
    kafka_manager = KafkaManager(kafka_config)
    data_parser = DataParser()
    listener = Listener()
    manager = Manager()

    #Logic

if __name__ == "__main__":
    main()