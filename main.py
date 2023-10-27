from random import randint


class Character:
    def __init__(self, name, damage, protection, special_skill, special_values) -> None:
        self.name = name
        self.damage = damage
        self.protection = protection
        self.special_skill = special_skill
        self.special_values = special_values
        pass

    def attack(self):
        return (f'{self.name} нанёс урон противнику равный '
                f'{5 + randint(self.damage)}')
        

    def defence(self):
        return (f'{self.name} блокировал {10 + randint(self.protection)} урона')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'«{self.special_skill} {self.special_values}»')














