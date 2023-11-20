
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


@error_handler
def create_table():
    global my_dict
    my_dict = {}
    return my_dict



@error_handler
def hello():
    print("How can I help you?")



@error_handler
def save_user(name, telephone):
    my_dict[name.title()] = telephone




@error_handler
def get_all_users():
    my_dict.items()
    print(my_dict)



@error_handler
def get_telephone_user(name):
    for kay in my_dict:
        if kay == name:
            print(my_dict.get(name))



@error_handler
def update_user(name, telephone):
    for kay in my_dict.values():
        if kay == name:
            my_dict.pop(name)
        my_dict[name] = telephone




if __name__ == '__main__':
    print("hello world")
