import random


class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Character: name: {} level: {}'.format(
            self.name, self.level
        )

    def get_attack_roll(self):
        return random.randint(1, 12) * self.level


class Hero(Character):
    # this isnt necessary if no Hero specific stuff added, can just inherit init from Character
    def __init__(self, name, level):
        # more Hero specific stuff
        super().__init__(name, level)

    def attack(self, monster):
        print('{} attacks {}'.format(
            self.name,
            monster.name
        ))

        hero_attack = self.get_attack_roll()
        monster_attack = monster.get_attack_roll()

        print('{} attack {}'.format(self.name, hero_attack))
        print('{} attack {}'.format(monster.name, monster_attack))

        if hero_attack >= monster_attack:
            print('{} defeated {}'.format(self.name, monster.name))

            return True
        else:
            print('{} lost to {}'.format(self.name, monster.name))

            return False


class Animal(Character):
    def __init__(self, name, level, is_angry):
        super().__init__(name, level)

        self.is_angry = is_angry

    def get_attack_roll(self):
        if self.is_angry:
            print('{} is angry! +20 attack!'.format(self.name))
            return super().get_attack_roll() + 20
        else:
            return super().get_attack_roll()


class Monster(Character):
    def __init__(self, name, level, has_weapon):
        super().__init__(name, level)

        self.has_weapon = has_weapon

    def get_attack_roll(self):
        if self.has_weapon:
            print('{} has a weapon! x2 attack!'.format(self.name))
            return super().get_attack_roll() * 2
        else:
            return super().get_attack_roll()