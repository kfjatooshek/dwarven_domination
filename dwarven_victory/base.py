class GameObject:
    def __init__(self, name: str, avatar: str = None) -> None:
        self.name = name
        self.avatar = avatar

    def _str__(self):
        return (f'{'Name: ':<30}{self.name:>20}\n'
                f'{'Avatar ':<30}\n{self.avatar}\n')

