import random
import dwarven_victory.character.character_stats_dict as character_stats_dict
from dwarven_victory.base import GameObject


class CreateCharacter(GameObject):
    def __init__(self, name: str = None, avatar: str = None, race: str = None,
                 hp: int = 100, strength: int = 100, exp: int = 0, level: int = 0,
                 race_attributes: dict = None, weapon_slots: int = 2, armor_slots: int = 2,
                 weapon: object = None, armor: object = None) -> None:
        super().__init__(name, avatar)
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

        self.adjust_character_stats()

    def __str__(self):
        return (f"{'Name: ':<30}{self.name:>20}\n"
                f"{'Experience: ':<30}{self.exp:>20}\n"
                f"{'Level: ':<30}{self.level:>20}\n"
                f"{'This is how you look like:':<30}{self.avatar}\n\n"
                f"{'Your weapon:':<30}{self.weapon}")

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


class DwarvenCharacter(CreateCharacter):
    def __init__(self, name: str = None, avatar: str = None) -> None:
        race = 'dwarf'
        race_attributes = character_stats_dict.race_attributes.get(race, {})
        super().__init__(name, avatar, race, race_attributes=race_attributes)


class ElvenCharacter(CreateCharacter):
    def __init__(self, name: str = None, avatar: str = None) -> None:
        race = 'elf'
        race_attributes = character_stats_dict.race_attributes.get(race, {})
        super().__init__(name, avatar, race, race_attributes=race_attributes)



