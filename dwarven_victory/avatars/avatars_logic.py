import time
from dwarven_victory.avatars.avatars_design import avatars


def time_sleep(sleep_time=1):
    time.sleep(sleep_time)


def pick_avatar(avatar_type):
    # TODO make this function accept only numbers in the range of length of the avatar list
    avatars_list = avatars.get(avatar_type)
    print(f"Here is the list of available avatars:")

    for i, (element, avatar) in enumerate(avatars_list.items(), 1):

        print(f'{'Number:':<20}{i:^10}\n'
              f'{'Avatar name:':<20}{element:^10}\n'
              f'{'The Avatar: ':<20}\n{avatar['avatar']}\n\n')

        time_sleep()

    chosen_avatar_number = int(input("Please choose the character's avatar by typing the corresponding number:\n"))-1
    chosen_avatar_name = list(avatars_list.keys())[chosen_avatar_number]
    chosen_avatar = avatars_list.get(chosen_avatar_name).get('avatar')

    return chosen_avatar


