
my_dict = {"Lol:": "123"}



def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner






def hello(_):
    return "How can I help you?"

def good_bye(_):
    return 'Good bye!'

def unknown_command(_):
    return """this command is not valid!
            Enter correct commands please!
    
"""

@error_handler
def save_user(data):
    name, telephone, *_ = data
    my_dict[name.title()] = telephone
    return f'User with name {name} and phone {telephone} was added!'




@error_handler
def get_all_users(_):
    result = []
    for name, telephone in my_dict.items():
        result.append(f'{name} - {telephone}')
    return result



@error_handler
def get_telephone_user(data):
    return f'The phone number is: {my_dict[data[0]]}'



@error_handler
def update_user(data):
    name, telephone, *_ = data
    for kay in my_dict.values():
        if kay == name:
            my_dict.pop(name)
        my_dict[name] = telephone
        return f'The phone number for name {name} was changed!'




if __name__ == '__main__':
    print("hello world")
