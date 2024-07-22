import random
import time
# TODO this whole file should be refactored to a class


def time_sleep(sleep_time = 1):
    time.sleep(sleep_time)

# creating a list of tuples containing avatar corresponding number, name and design


def dwarf_avatars():
    return [
        (1, 'Happy Dwarf', r"""
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
"""),
        (2, 'Smiling Dwarf', r""""
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
"""),
        (3, 'Regular Dwarf', r""""
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
""")]


def enemy_avatars():
    return [(1, 'Deadly Dragon', r"""
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
        """),
            (2, 'Evil Sauron', r"""
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
        """)]


def pick_avatar(race_avatars):
    # TODO make this function accept only numbers in the range of length of the avatar list
    print(f"Here is the list of available avatars:")

    for i, j, k in race_avatars():
        print(f'{'Number:':<20}{i:^10}\n{'Avatar name:':<20}{j:^10}\n{k}\n\n\n')
        time_sleep()

    chosen_avatar = int(input("please choose the character's avatar by typing the corresponding number:\n"))-1
    print(f'This is how you will look like:{race_avatars()[chosen_avatar][2]}')
    return race_avatars()[chosen_avatar][2]





