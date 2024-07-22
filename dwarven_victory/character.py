import random
import avatars
import items


class CreateCharacter:
    def __init__(self):
        self.race = None
        self.name = None
        self.avatar = None
        self.exp = 0
        self.level = 0
        self.HP = 1000
        self.MP = 1000
        self.strength = 100
        self.weapon_slots = 1
        self.armor_slots = 2
        self.weapon = [None]
        self.armor = [None]
        self.attack = self.strength  # + self.weapon[0].attack
        self.race_attributes = {}
        # self.defence = 100 + self.armor[0]

    def __str__(self):
        return (f'{'Name: ':<20}{self.name:>20}\n'
                f'{'Race: ':<20}{self.race:>20}\n'
                f'{'Experience: ':<20}{self.exp:>20}\n'
                f'{'Level: ':<20}{self.level:>20}\n'
                f'{'Strength ':<20}{self.strength:>20}\n'
                f'{'Attack: ':<20}{self.attack:>20}\n'
                f'{'HP: ':<20}{self.HP:>20}\n'
                f'{'MP: ':<20}{self.MP:>20}\n\n'
                f'{'This is how you look like:':<30}{self.avatar}')

    @staticmethod
    def choose_avatar():
        return avatars.pick_avatar(avatars.dwarf_avatars)

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
        self.avatar = self.choose_avatar()
        # self.weapon.append(items.WeaponGenerator(dwarf))
        self.race_attributes = {'hp_modifier': (1, 2), 'mp_modifier': (0.1, 0.2), 'str_modifier': (1, 2)}
        self.adjust_character_stats()


class ElvenCharacter(CreateCharacter):
    # container for future development of another class
    pass


dwarf = DwarfCharacter()

print(dwarf)



