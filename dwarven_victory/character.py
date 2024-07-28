import random
from base import GameObject
from dwarven_victory import avatars
from dwarven_victory import items
import items.items_logic as items


class CreateCharacter(GameObject):
    def __init__(self):
        super().__init__()
        self.race = None
        self.exp = 0
        self.level = 0
        self.weapon_slots = 1
        self.armor_slots = 2
        self.weapon = None
        self.armor = None
        self.race_attributes = {}

    def __str__(self):
        return (f'{'Race: ':<30}{self.race:>20}\n'
                f'{'Experience: ':<30}{self.exp:>20}\n'
                f'{'Level: ':<30}{self.level:>20}\n'
                f'{'This is how you look like:':<30}{self.avatar}\n\n'
                f'{'Your weapon:':<30}{self.weapon[2]}\n{self.weapon[0]}')

    @staticmethod
    def chose_weapon():
        return items.pick_weapon()

    def adjust_character_stats(self):
        self.hp = int(self.HP * random.uniform(self.race_attributes['hp_modifier'][0],
                                               self.race_attributes['hp_modifier'][1]))
        self.strength = int(self.strength * random.uniform(self.race_attributes['str_modifier'][0],
                                                           self.race_attributes['str_modifier'][1]))

    def got_hit(self):
        self.hp = self.hp-100


class DwarfCharacter(CreateCharacter):

    def __init__(self):
        super().__init__()
        self.race = "dwarf"
        self.name = input("Please enter your character's name:")
        self.avatar = avatars_logic.pick_avatar(avatars_design.dwarf_avatars)
        self.race_attributes = {'hp_modifier': (1, 2),
                                'str_modifier': (1, 2)}
        self.adjust_character_stats()
        self.weapon = items.pick_weapon()
        self.strength += int(self.weapon[1])


class ElvenCharacter(CreateCharacter):
    # container for future development of another class
    pass

x = DwarfCharacter
print(x)