import random
import dwarven_victory.character.character_stats_dict as character_stats_dict
from dwarven_victory.base import GameObject


class CreateCharacter(GameObject):
    def __init__(self,
                 name: str,
                 avatar: str = "",
                 hp: int = 100,
                 strength: int = 100,
                 exp: int = 0,
                 level: int = 0,
                 race: str = None) -> None:

        super().__init__(name, avatar)
        self.name = name
        self.avatar = avatar
        self.hp = hp
        self.strength = strength
        self.exp = exp
        self.level = level
        self.weapon_slots = 1
        self.armor_slots = 2
        self.weapon = None
        self.armor = None
        self.race = race

# TODO this str method needs to be aligned with the str of the base.py
    def __str__(self):
        return (f'{'Name: ':<30}{self.name:>20}\n'
                f'{'Experience: ':<30}{self.exp:>20}\n'
                f'{'Level: ':<30}{self.level:>20}\n'
                f'{'This is how you look like:':<30}{self.avatar}\n\n'
                f'{'Your weapon:':<30}{self.weapon}')

    def adjust_character_stats(self):
        race_attr = character_stats_dict.race_attribute().get(self.race)
        self.hp = int(self.hp * random.uniform(race_attr.get('str_min_multipl'),
                                               race_attr.get('str_max_multipl')))
        self.strength = int(self.strength * random.uniform(race_attr.get('hp_min_multipl'),
                                                           race_attr.get('hp_max_multipl')))


class DwarvenCharacter(CreateCharacter):
    def __init__(self, name: str, avatar: str,  race: str = "dwarf") -> None:
        super().__init__(name, avatar)
        self.race = race
        self.name = name
        self.avatar = avatar
        self.adjust_character_stats()


class ElvenCharacter(CreateCharacter):
    # container for future development of another class
    pass


