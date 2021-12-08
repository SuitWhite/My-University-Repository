def input_and_check_size():
    while True:
        check = 0
        value = 0
        try:
            value = int(input('Enter size of list: '))
        except ValueError:
            print('You entered wrong data!')
            check = 1
        if value < 0:
            print('You entered negative number!')
            check = 1
        if check == 0:
            break
    return value


def input_check_list_element_or_interval_limit():
    while True:
        check = 0
        element = 0
        try:
            element = int(input('Enter: '))
        except ValueError:
            print('You entered wrong data!')
            check = 1
        if check == 0:
            break
    return element


def input_and_check_index(list_size):
    while True:
        check = 0
        index = 0
        try:
            index = int(input('Enter index: '))
        except ValueError:
            print('You entered wrong data!')
            check = 1
        if index < 0 or index > list_size-1:
            print('There is no such index!')
            check = 1
        if check == 0:
            break
    return index