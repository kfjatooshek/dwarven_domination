class CreateCharacter:
    def __init__(self):
        self.type = None
        self.name = None
        self.HP = 1000
        self.MP = 1000
        self.strength = 100
        self.agility = 100
        self.intelligence = 100
        self.weapon = None
        self.avatar = None

    def __str__(self):
        return f'Name: {self.name: <30} /n {self.avatar}'


    def who_are_you(self):
        print(self.name)

    def got_hit(self):
        self.HP = self.HP-100


class DwarfCharacter(CreateCharacter):
    def __init__(self):
        super().__init__()
        self.type = "Dwarf"
        self.name = "Ghen"
        self.HP = self.HP*1
        self.MP = 10
        self.strength = 1000
        self.agility = 10
        self.weapon = "Axe"




class ElvenCharacter(CreateCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Elivarien"
        self.HP = self.HP*0.1
        self.MP = 1000


dwarf = DwarfCharacter()
print(dwarf.HP, '\n', dwarf.name)
dwarf.got_hit()
print(dwarf.HP, '\n', dwarf.name)
dwarf.got_hit()
print(dwarf.HP, '\n', dwarf.name)

elf = ElvenCharacter()
print(elf.HP, '\n', elf.name)
elf.got_hit()
print(elf.HP, '\n', elf.name)
elf.got_hit()
print(elf)

