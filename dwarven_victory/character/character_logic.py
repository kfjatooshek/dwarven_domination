import random
import dwarven_victory.character.character_stats_dict as character_stats_dict
from dwarven_victory.base import GameObject
from dwarven_victory.enemies.enemy_logic import pick_enemy
from dwarven_victory.fight.fight_logic import fight_enemy


class CreateCharacter(GameObject):
    def __init__(self, race: str,
                 hp: int = 100, strength: int = 100, exp: int = 0, level: int = 0,
                 race_attributes: dict = None, weapon_slots: int = 2, armor_slots: int = 2,
                 weapon: object = None, armor: object = None, obj_type: str = 'character') -> None:
        super().__init__()
        self.race = race
        self.hp = hp
        self.strength = strength
        self.exp = exp
        self.level = level
        self.race_attributes = race_attributes or {}
        self.weapon_slots = weapon_slots
        self.armor_slots = armor_slots
        self.weapon = weapon
        self.armor = armor
        self.obj_type = obj_type
        self.adjust_character_stats()
        self.base_strength = self.strength
        self.base_hp = self.hp

    def __str__(self):
        return (f"{'Name: ':<30}{self.name:>20}\n"
                f"{'This is how you look like:':<30}{self.avatar}\n\n"
                f"{'Your weapon:':<30}{self.weapon.avatar}\n\n"
                f"{'Your armor:':<30}{self.armor.avatar}\n")

    def print_stats(self):
        print(f"{'Name: ':<30}{self.name:>20}\n"
                f"{'Experience: ':<30}{self.exp:>20}\n"
                f"{'Level: ':<30}{self.level:>20}\n"
                f"{'Strength: ':<30}{self.strength:>20}\n"
                f"{'HP: ':<30}{self.hp:>20}\n")

    def adjust_character_stats(self):
        if self.race_attributes:
            self.hp = int(self.hp * random.uniform(
                self.race_attributes.get('hp_min_multipl', 1),
                self.race_attributes.get('hp_max_multipl', 1)
            ))
            self.strength = int(self.strength * random.uniform(
                self.race_attributes.get('str_min_multipl', 1),
                self.race_attributes.get('str_max_multipl', 1)
            ))

    def adjust_stats_from_items(self):
        self.hp += self.weapon.hp + self.armor.hp
        self.strength += self.weapon.strength + self.armor.strength
        self.base_hp = self.hp
        self.base_strength = self.strength


def pick_race():
    available_races = character_stats_dict.race_attributes.keys()

    print("Here is the list of character's races available")
    for k, v in enumerate(available_races, 1):
        print(f'{k:<10}{v:<10}')
    available_races_list = list(available_races)
    players_race_number = int(input("Please enter the corresponding number to select your character's race: ")) - 1
    players_race = available_races_list[players_race_number]

    return players_race


def choose_action(players_character):
    possible_actions = {1: 'look at yourself', 2: 'check your stats', 3: 'fight the enemy!', 4: 'quit the game'}
    while True:
        print(f'Here are the things you can do in this world:')
        for i, action in possible_actions.items():
            print(f'{i:<10}{action:>20}')
        chosen_action = int(input("What do you want to do? Please enter the corresponding number."))
        if chosen_action == 1:
            print(players_character)
            continue
        if chosen_action == 2:
            players_character.print_stats()
        if chosen_action == 3:
            fight_enemy(players_character, pick_enemy("enemy"))
        if chosen_action == 4:
            print('I hope you had a great time! See you next time!')
            break
        else:
            continue


class DwarvenCharacter(CreateCharacter):
    def __init__(self) -> None:
        race = 'dwarf'
        race_attributes = character_stats_dict.race_attributes.get(race, {})
        super().__init__(race, race_attributes=race_attributes)


class ElvenCharacter(CreateCharacter):
    def __init__(self) -> None:
        race = 'elf'
        race_attributes = character_stats_dict.race_attributes.get(race, {})
        super().__init__(race, race_attributes=race_attributes)
