import time
# TODO this whole file should be refactored to a class
# TODO maybe the avatars themselves (as a graphic) should be exported somewhere separate file, to not to mess with the code


def time_sleep(sleep_time=1):
    time.sleep(sleep_time)

# creating a list of tuples containing avatar corresponding number, name and design


def pick_avatar(avatars_list):
    # TODO make this function accept only numbers in the range of length of the avatar list
    print(f"Here is the list of available avatars:")

    for i, j, k in avatars_list:
        print(f'{'Number:':<20}{i:^10}\n{'Avatar name:':<20}{j:^10}\n{k}\n\n\n')
        time_sleep()

    chosen_avatar = int(input("please choose the character's avatar by typing the corresponding number:\n"))-1
    print(f'This is how you will look like:{avatars_list[chosen_avatar][2]}')
    return avatars_list[chosen_avatar][2]


