
from t_main.parser import parser

def user_input(user):
    game = True
    commands = ["add", "hello", "change", "phone", "show all", "delete"]
    for command in commands:
        if user in input([command]).lower():
            return command

        good_bye = ["good bye", "close", "exit"]
        if user in good_bye:
            print("Good bye!")
            game = False
        else:
            parser(user)
    return game

def main():
    gameloop = True
    while gameloop:
        print('ask me:')
        rep = input().lower()
        result = parser(rep)
        print(result)

if __name__ == '__main__':
    main()