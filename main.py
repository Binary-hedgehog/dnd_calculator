class Base:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.speed = 0
        self.state = {}
        self.skills = []
    def check_state(self):
        pass

    def get_skill_note(self):
        pass


class State:

    def __init__(self, name):
        pass


    # тут надо описать механику эффектов, кровотечений и прочего дерьма


class Person(Base):
    def __init__(self, name):
        super.__init__()
        pass

    # def get_current_state(self):
    #     return self.hp, self.mp

    # функция которая возвращает все параметры? Но только по умному


"""
1. Инициализация персонажа посредством поиска его в monsters.json
2. Список таких персонажей
3. Функция снижающая и считающая урон на основе типа атаки - должна понижать здоровье цели
4. Автофункция, которая каждый ход проверяет статус цели, понижает здоровье, выводит информацию о её текущем состоянии
5. Функция чтения команд и функция обработчик команд - возможно стоит начать как раз с этого?
6. -??!
"""

class Fight:
    def __init__(self):
        self.characters_list = []

    def add_monstr_to_fight(self, name):
        self.characters_list.append(Person(name))

    def


def main():
    new_fight = 0
    for
















