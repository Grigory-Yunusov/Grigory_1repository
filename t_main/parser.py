from handler import *


def parser(user_input):

    commands = user_input.split(' ')
    commands[0] # add, change_name, change_phone, phone, show, show all, delete

    if commands[0] == 'hello':
        return hello()
    if commands[0] == 'add':
        return save_user(commands[1], commands[2])
    if commands[0] == 'change':
        return update_user(commands[1], commands[2])
    if commands[0] == 'phone':
        return get_telephone_user(commands[1], commands[2])
    if commands[0] == 'show all':
        return get_all_users()



if __name__ == '__main__':
    parser.parser("user")