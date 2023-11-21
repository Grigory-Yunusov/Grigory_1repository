
from t_main.parser import parser

def main():
    flag = True
    while flag:
        user_input = input('Enter command>>> ')
        if user_input in ('good_bye', 'exit', 'close', '.'):
            flag = False
        handler, data = parser(user_input)
        try:
            result = handler(data)
            print(result)
        except KeyError:
            print('Unknown command')

if __name__ == '__main__':
    main()
