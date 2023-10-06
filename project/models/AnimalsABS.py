from abc import ABC, abstractmethod

class Animals(ABC):

    def __init__(self, name, birthday, command):
        self.name = name
        self.birthday = birthday
        self.command = command

    def get_name(self):
        return self.__name
    
    def get_birthday(self):
        return self.__birthday
    
    def get_command(self):
        return self.__command
    
    @abstractmethod
    def print_animal(self):
        pass
