from handler import *


def parser(user_input):
    action = user_input.split()[0].lower()
    data = user_input.split()[1:]
    try:
        handler = COMMANDS[action]
    except KeyError:
        handler = unknown_command
        if not action or action == '.':
            handler = good_bye
    return handler, data


COMMANDS = {
    'hello': hello,
    'add': save_user,
    'change': update_user,
    'phone': get_telephone_user,
    'show_all': get_all_users,
    'good_bye': good_bye,
    'exit': good_bye,
    'close': good_bye
}


if __name__ == '__main__':
    parser("user")