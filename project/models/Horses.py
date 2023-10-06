from PackAnimalsABS import PackAnimals

class Horses(PackAnimals):

    def __init__(self, name, birthday, command):
        super().__init__(name, birthday, command)

    def eat(self):
        pass

    def medicines(self):
        pass

    def print_animal(self):
        print(f"Имя коня или лошади: {self.get_name()}",
              f"Дата рождения: {self.get_birthday()}",
              f"Команды: {self.get_command()}")