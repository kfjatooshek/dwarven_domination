import random
from avatars import avatars_design, avatars_logic
import items


class CreateCharacter:
    def __init__(self):
        self.race = None
        self.name = None
        self.avatar = None
        self.exp = 0
        self.level = 0
        self.HP = 1000  # +armor.HP[0] # TODO introduce armors (items.py armor function)
        self.MP = 1000
        self.strength = 100
        self.weapon_slots = 1
        self.armor_slots = 2
        self.weapon = None
        self.armor = None
        self.race_attributes = {}

    def __str__(self):
        return (f'{'Name: ':<30}{self.name:>20}\n'
                f'{'Race: ':<30}{self.race:>20}\n'
                f'{'Experience: ':<30}{self.exp:>20}\n'
                f'{'Level: ':<30}{self.level:>20}\n'
                f'{'Strength ':<30}{self.strength:>20}\n'
                f'{'HP: ':<30}{self.HP:>20}\n'
                f'{'MP: ':<30}{self.MP:>20}\n\n'
                f'{'This is how you look like:':<30}{self.avatar}\n\n'
                f'{'Your weapon:':<30}{self.weapon[2]}\n{self.weapon[0]}')


    @staticmethod
    def chose_weapon():
        return items.pick_weapon()

    def adjust_character_stats(self):
        self.HP = int(self.HP * random.uniform(self.race_attributes['hp_modifier'][0],
                                               self.race_attributes['hp_modifier'][1]))
        self.MP = int(self.MP * random.uniform(self.race_attributes['mp_modifier'][0],
                                               self.race_attributes['mp_modifier'][1]))
        self.strength = int(self.strength * random.uniform(self.race_attributes['str_modifier'][0],
                                                           self.race_attributes['str_modifier'][1]))

    def got_hit(self):
        self.HP = self.HP-100


class DwarfCharacter(CreateCharacter):

    def __init__(self):
        super().__init__()
        self.race = "dwarf"
        self.name = input("Please enter your character's name:")
        self.avatar = avatars_logic.pick_avatar(avatars_design.dwarf_avatars)
        self.race_attributes = {'hp_modifier': (1, 2),
                                'mp_modifier': (0.1, 0.2),
                                'str_modifier': (1, 2)}
        self.adjust_character_stats()
        self.weapon = items.pick_weapon()
        self.strength += int(self.weapon[1])


class ElvenCharacter(CreateCharacter):
    # container for future development of another class
    pass

