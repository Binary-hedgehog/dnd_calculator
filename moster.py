from main import roll_dice, get_json_data
from person import Person


class Monster(Person):

    def __init__(self, name):
        self.arch_type = ""
        self.type = ""
        self.coins = 0
        self.skills = []
        self.name = name
        self.set_monster_by_name(name)
        self.cur_hp = self.max_hp
        self.cur_mp = self.max_mp
        self.cur_velocity = self.max_velocity

    def set_monster_by_name(self, name):
        monsters_dict = get_json_data("monsters.json")
        # found = False
        for monster in monsters_dict:
            if name == monster["имя"]:
                self.arch_type = monster["архитип"]
                self.type = monster["тип"]
                self.max_hp = monster["здоровье"]
                self.max_mp = monster["мана"]
                self.max_velocity = monster["скорость"]
                self.coins = monster["коины"]
                self.skills = monster["способности"]
                self.immunity = monster["иммунитет"]
                self.resistance = monster["сопротивление"]
                self.sustainability = monster["устойчивость"]
                self.vulnerabilities = monster["уязвимость"]
                # found = True
                break
        # TODO return Found if False - incorrect name

    def get_skills(self):
        return ", ".join(self.skills)

    def roll_dice_plus_coin(self):
        return roll_dice(1, 20) + str(self.coins)
