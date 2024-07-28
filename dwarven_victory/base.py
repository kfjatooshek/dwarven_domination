class GameObject:
    def __init__(self, name: str, avatar: str, hp: int) -> None:
        self.name = ""
        self.avatar = ""
        self.hp = 0
        self.strength = 0

    def _str__(self):
        return (f'{'Name: ':<30}{self.name:>20}\n'
                f'{'Strength ':<30}{self.strength:>20}\n'
                f'{'HP: ':<30}{self.hp:>20}\n')