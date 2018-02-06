import random
import time

import characters


def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------------')
    print('        adventure')
    print('-------------------------')


def game_loop():
    hero = characters.Hero('mc', 75)

    monsters = []

    number_of_tigers = random.randint(1, 3)

    for i in range(0, number_of_tigers):
        is_angry = random.randint(0, 1) == 0

        monsters.append(characters.Animal('tiger', 25, is_angry))

    number_of_giants = random.randint(1, 3)

    for i in range(0, number_of_giants):
        has_weapon = random.randint(0, 1) == 0

        monsters.append(characters.Monster('giant', 50, has_weapon))

    print(monsters)

    in_game = True

    while in_game:
        active_monster = random.choice(monsters)

        print('a lvl {} {} appears! '.format(active_monster.level, active_monster.name))

        player_command = input('[a]ttach, [r]un, [l]ook, or e[x]it game? ')

        if player_command == 'a':
            if hero.attack(active_monster):
                monsters.remove(active_monster)
            else:
                print('{} needs to recover...'.format(hero.name))

                time.sleep(3)

                print('{} is ready for battle again!'.format(hero.name))
        elif player_command == 'r':
            print('running')
        elif player_command == 'l':
            print('{} sees: '.format(hero.name))

            for monster in monsters:
                print('lvl {} {}'.format(monster.level, monster.name))
        elif player_command == 'x':
            print('exit')

            in_game = False
        else:
            print('invalid command')

        if not monsters:
            print('{} defeated all the monsters!'.format(hero.name))

            in_game = False


if __name__ == '__main__':
    main()
