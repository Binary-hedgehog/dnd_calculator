import random


class Person:
    name = ""
    max_hp = 0
    max_mp = 0
    cur_hp = max_hp
    cur_mp = max_mp
    velocity = 0
    state = {}
    isDead = False
    immunity = []
    resistance = []
    sustainability = []
    vulnerabilities = []

    def get_damage(self, value):
        self.cur_hp -= value
        if self.cur_hp <= 0:
            self.cur_hp = 0
            self.isDead = True

    # Урон с расчетом зависимостей от State и типа урона
    # TODO возможно сюда стоит добавить значение бросков кубика на попадание и защиту?
    def get_difficult_damage(self, value, damage_type):
        pass

    def lose_mp(self, value):
        self.cur_mp -= value
        if self.cur_mp <= 0:
            self.cur_mp = 0
            # TODO повесить истощение маны

    def restore_hp(self, value):
        self.cur_hp += value
        if self.cur_hp > self.max_hp:
            self.cur_hp = self.max_hp

    def restore_mp(self, value):
        # TODO добавить проверку на наличие истощения маны
        self.cur_mp += value
        if self.cur_mp > self.max_mp:
            self.cur_mp = self.max_mp


class Monster(Person):

    def __init__(self, name):
        self.coins = 0
        self.skills = []
        self.damage = ""
        self.type = ""
        self.arch_type = ""
        self.set_monster_by_name(name)

    # TODO добавить создание монстра из monsters.json
    def set_monster_by_name(self, name):
        pass

    def get_skills(self):
        pass

    def roll_dice_plus_coin(self):
        return roll_dice(1, 20) + str(self.coins)


class Character(Person):
    # TODO подумать о том как инициализировать персонажа и надо ли оно вообще
    def __init__(self, name, palyer_name, char_class, race, stats, max_hp, max_mp):
        self.char_class = ""
        self.race = ""
        self.stats = "???"  # TODO подумать над реализацией статов персонажа и усе такое

    def set_max_hp(self, value):
        self.max_hp = value

    def set_max_mp(self, value):
        self.max_mp = value

    # TODO В конце партии формировать персонажа в виде словаря и потом генерировать из этого всего json
    def get_character_as_json(self):
        pass


class Fight:

    def __init__(self):
        self.fight_dict = {}

    # Когда в бою участвуют несколько одинаковых монстров им нужно придумывать псевдонимы
    def add_monster_to_fight(self, name, pseudonym=""):
        name_in_dict = pseudonym if pseudonym else name
        self.fight_dict[name_in_dict] = Monster(name)

    # TODO стоит ли добавить сюда вывод чего-то еще или сделать отдельную функцию с full info
    def get_fight_list(self):
        return ", ".join([name for name in self.fight_dict if not self.fight_dict[name].isDead])

    # TODO необходимость под вопросом как и старт боя
    def end_fight(self):
        pass


""" TODO LIST
1. Инициализация монстра посредством поиска его в monsters.json
1.1 Перенести всех из бестиария
2. Использование damage_type_list для проверки уменьшения урона от конкретного типа
3. Реализовать до конца класс Fight
3.1 Добавление монстров
3.2 Новый ход 
3.3 Удаление монстров и перенос их в dead_list
4. Написать требования к API
5. Заполнить словать states_duration_dict
6. В классе Fight сделать обработчик статусов, включенный в обработчик нового хода  
"""


def roll_dice(dice_number, edges):
    return ", ".join([str(random.randint(1, edges)) for i in range(dice_number)])


def get_skill_by_name():
    pass


# Словарь...или список? Со всеми видами урона
damage_type_list = ["fire", "frost", "lightning", "holy", "filth", "pricking", "cutting", "crushing"]
states_duration_dict = {"burned": 1, "bleeding_low": 3, "bleeding_medium": 4, "high_bleeding": 999, }
# словарь со всеми способностями: слабый яд на хп, ошеломление, и все, что поедт в State
# возможно это стоит определить где-то еще, вообще обработка state можно сделать отдельным классом, так как сложные механики
# в общем и целом TODO
ability_type_dict = {}
players_list = []

class B:
    def foo(self):
        return 1

a = eval("foo")

print(B().a)
