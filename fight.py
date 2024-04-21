from moster import Monster


class Fight:

    def __init__(self):
        self.fight_dict = {}
        self.death_list = []

    # Когда в бою участвуют несколько одинаковых монстров им нужно придумывать псевдонимы
    def add_monster_to_fight(self, name, pseudonym=""):
        name_in_dict = pseudonym if pseudonym else name
        self.fight_dict[name_in_dict] = Monster(name)

    def new_move(self, name):
        monster = self.fight_dict[name]

    def check_state(self, monster):
        # 1 - проход и убирание пустых states
        # 2 - пошаговое выполнение текущих states
        # 2.1 - уменьшение duration
        # 3 - вернуть монстра обратно или перезаписать в текущем словаре (думаю второе)

        #for state in
        pass

    # TODO стоит ли добавить сюда вывод чего-то еще или сделать отдельную функцию с full info
    def get_fight_list(self):
        return ", ".join([name for name in self.fight_dict if not self.fight_dict[name].isDead])

    # TODO необходимость под вопросом как и старт боя
    def end_fight(self):
        self.fight_dict = {}
        self.death_list = []

