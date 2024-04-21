from moster import Monster


class State:

    def __init__(self, monster: Monster):
        self.state_duration_check(monster)

    def state_duration_check(self, monster: Monster):
        states = monster.state
        for state_name, duration in states.items():
            if duration <= 0:
                monster.state.pop(state_name)  # TODO можно добавить вывод оконченных состояний

    def state_main(self, monster: Monster):
        states = monster.state
        for state_name, duration in states.items():
            if "poison" in state_name:
                pass
                if monster.isDead:
                    break
            elif state_name == "birned":
                pass
                if monster.isDead:
                    break
            elif "frosted" in state_name:
                pass