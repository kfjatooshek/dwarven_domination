class GameObject:
    def __init__(self, name: str = None, avatar: str = None, hp: int = 10, strength: int = 10, obj_type: str = None) -> None:
        self.name = name
        self.avatar = avatar
        self.hp = hp
        self.str = strength
        self.obj_type = obj_type

    def __str__(self):
        return (f'{'Name: ':<30}{self.name:>20}\n'
                f'{'Avatar ':<30}\n{self.avatar}\n')

