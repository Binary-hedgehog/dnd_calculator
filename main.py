import json
import random

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

# TODO roll dice by **kwargs
def roll_dice(dice_number, edges):
    return ", ".join([str(random.randint(1, edges)) for i in range(dice_number)])

# TODO create skills.json
def get_skill_by_name():
    pass

def get_available_monsters():
    monsters_dict = get_json_data("monsters.json")
    return ", ".join([monster["имя"] for monster in monsters_dict])

def get_json_data(path):
    try:
        with open(path, encoding="utf-8") as file:
            out = json.load(file)
    except:
        print(f"Ошибка чтения файла {path}")
        input("Хорошо не стало. Нажмите любую кнопку для завершения")
        exit()
    return out

# Словарь...или список? Со всеми видами урона
damage_type_list = ["fire", "frost", "lightning", "holy", "cursed", "pricking", "cutting", "crushing", "poison"]
states_duration_dict = {"burned": 1, "bleeding_low": 3, "bleeding_medium": 4, "high_bleeding": 999, "mild_frostbite": 123,
                        "average_frostbite": 123, "several_frostbite": 0}  # TODO add more
# словарь со всеми способностями: слабый яд на хп, ошеломление, и все, что поедт в State
# возможно это стоит определить где-то еще, вообще обработка state можно сделать отдельным классом, так как сложные механики
# в общем и целом TODO
ability_type_dict = {}
players_list = []

#
# class B:
#     a = 3
#
#
# class C:
#
#     def foo(self, b: B):
#         b.a+=1
#
#
# #a = eval("foo")
#
# cl = B()
#
# C().foo(cl)

