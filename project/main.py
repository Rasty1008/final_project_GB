from project.Database.DB_config import config_db_init
from project.Database.DB_creating import create_db_human_friends
from project.models.Camels import Camels
from project.models.Cats import Cats
from project.models.Dogs import Dogs
from project.models.Donkeys import Donkeys
from project.models.Hamsters import Hamsters
from project.models.Horses import Horses
from project.View.Menu import ls_menu

if __name__ == '__main__':
    print('\nPets accounting started')

    config = config_db_init()
    dog_1 = Dogs('Шарик', '2018-06-12', 'come here')
    cat_1 = Cats('Мурзик', '2023-05-19', 'come here')
    hamster_1 = Hamsters('Прошка', '2016-07-10', 'run')
    camel_1 = Camels('Шустрый', '2018-03-12', 'transport')
    donkey_1 = Donkeys('Высокий', '2023-02-19', 'transport')
    horse_1 = Horses('Упертый', '2016-07-02', 'jump')
    create_db_human_friends(config)
    ls_menu(config)