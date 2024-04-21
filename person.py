import math


class Person:
    name = ""
    max_hp = 0
    max_mp = 0
    cur_hp = max_hp
    cur_mp = max_mp
    max_velocity = 0
    cur_velocity = max_velocity
    state = {}  # name : duration
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

    def get_difficult_damage(self, value, damage_type):
        if damage_type in self.immunity:
            # TODO - out "zero dammage"
            pass
        elif damage_type in self.resistance:
            self.get_damage(math.ceil(value * 0.5))
        elif damage_type in self.sustainability:
            self.get_damage(math.ceil(value * 0.75))
        elif damage_type in self.vulnerabilities:
            self.get_damage(math.ceil(value * 1.5))
        else:
            self.get_damage(value)

    def lose_mp(self, value):
        self.cur_mp -= value
        if self.cur_mp <= 0:
            self.cur_mp = 0
            self.state["mana_drain"] = 99

    def restore_hp(self, value):
        self.cur_hp += value
        if self.cur_hp > self.max_hp:
            self.cur_hp = self.max_hp

    def restore_mp(self, value):
        if "mana_drain" not in self.state:
            self.cur_mp += value
            if self.cur_mp > self.max_mp:
                self.cur_mp = self.max_mp
        else:
            # TODO - out "you cant restore mp - cause of drain"
            pass