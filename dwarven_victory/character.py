import random
import avatars


class CreateCharacter:
    def __init__(self):
        self.race = None
        self.name = None
        self.avatar = None
        self.HP = 1000
        self.MP = 1000
        self.strength = 100
        self.agility = 100
        self.intelligence = 100
        self.weapon_slots = 1
        self.armor_slots = 2
        self.weapon = [None]
        self.armor = [None]
        self.attack = 100 + self.strength #+ self.weapon[0].attack
        #self.defence = 100 + self.armor[0]

    def __str__(self):
        return f'{'Name: ':<10}{self.name:>20}\n{'Character race:':<20}{self.race:>10}\n{'HP: ':<10}{self.HP:>20}\n\n{'This is how you look like:':<30}{self.avatar}'

    def choose_avatar(self):
        self.avatar = avatars.AvatarGenerator.generate_dwarf_avatar()

    def got_hit(self):
        self.HP = self.HP-100


class DwarfCharacter(CreateCharacter):
    def __init__(self, name):
        super().__init__()
        self.race = "Dwarf"
        self.name = name
        self.avatar = CreateCharacter.choose_avatar()
        self.HP = int(self.HP * random.uniform(1, 2))
        self.MP = int(self.MP * random.uniform(0.1, 0.2))
        self.strength = int(self.strength * random.uniform(1, 2))
        self.agility = int(self.strength * random.uniform(0, 0.2))
        self.weapon = "Axe"



dwarf = DwarfCharacter("Periven")
print(dwarf)

