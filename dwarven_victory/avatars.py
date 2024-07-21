import random


class AvatarGenerator:
    dwarf_1 = """
         ____
        /    \\
       / ____ \\
      / / . . \\ \\
     | /   "   \\ |
      \\  \\___/  /
       \\_______/
         /   \\
        /____ \\
       /      \\
      /________\\
"""

    dwarf_2 = """
         ____
       _|____|_
      /  _  _  \\
     |  (o)(o)  |
     |    ()    |
      \\  \\__/  /
       \\______/
        |    |
       /| |  |\\
      / | |  | \\
     /__|_|__|__\\
"""
    dwarf_3 = """
         _____
        /     \\
       / () () \\
      |    ^    |
       \\  ===  /
        \\_____/
       /       \\
      /|  |||  |\\
     / |  |||  | \\
    /__|__|||__|__\\
"""

    enemy_dragon_avatar = """
                                   __====-_  _-====__
                        _--^^^#####//      \\#####^^^--_
                     _-^##########// (    ) \\##########^-_
                    -############//  |\^^/|  \\############-
                  _/############//   (@::@)   \\############\_
                 /#############((     \\//     ))#############\
                -###############\\    (oo)    //###############-
               -#################\\  / "" \  //#################-
              -###################\\/  (_)  \//###################-
             _#/|##########/\######(   /  \   )######/\##########|\#_
             |/ |#/\#/\#/\/  \#/\##\  \   /  /##/\#/\#/\#/\/  \#/\| \|
             \  |/ /\ / /\   / /\##\  \_/  /##/\ / /\   / /\  |/  /
               \   /\ /  / /\ / /\##|/   /##/\ / /\ /  / /\ /   /
                \ / /\ /  / /\ / /##/   /##/\ / /\ /  / /\ / \  /
                  \  /  / /   / /\##/   /##/\   /  / /  /  /
                   \/    \   /  /###|   /###\  /  /   /
                    \  / /\  / /\ /##/   /##\   / /\ / /
                     \   / /\   /\ /###|   /###\  /\   /
                      \ /\   /\   / /##/   /##\   / /\ / \
                        \ /\   /   /###|   /###\   /\ / 
                          \  /   / /##/   /##\   /\ /
                            \/  / ###|   /###\  /
                              \_/  \_/ \_/ \_/ \_/
        """

    enemy_sauron_avatar = """
              _.-._
           .'\  |  /'.
          /  \ | /    \
          |\/\ |/\/|   |   
          |\/\ |/\/|   |   
           \__/'\__/    
         _.-./      \.-._
       .'  .-_.   .-'_.  '.
      /  .-./\_.'\_.\-/.  \
      | /  / /   `   \ \  \ |
      |/  / |        | \  \|
          |            |
         /              \
        |   \  \  |  /   |
        |    | /|  |/ |   |
         \  |/_/    \_|\  /
          `.___  Sauron___.'
        """


    @classmethod
    def generate_dwarf_avatar(cls):
        return random.choice(cls.dwarf_avatars)

    @classmethod
    def generate_elf_avatar(cls):
        return random.choice(cls.elf_avatars)


