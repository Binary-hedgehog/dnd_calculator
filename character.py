from person import Person


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
