from PackAnimalsABS import PackAnimals

class Camels(PackAnimals):

    def __init__(self, name, birthday, command):
        super().__init__(name, birthday, command)

    def eat(self):
        pass

    def medicines(self):
        pass

    def print_animal(self):
        print(f"Имя верблюда: {self.get_name()}",
              f"Дата рождения: {self.get_birthday()}",
              f"Команды: {self.get_command()}")