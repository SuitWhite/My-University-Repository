from MyLinkedList import*


def menu():
    print('Menu:')
    print('1 - Input with keyboard')
    print('2 - Randomize in interval [a,b]')
    print('3 - Add element on position k')
    print('4 - Delete element from position k')
    print('5 - Calculate multiplication')
    print('6 - Print list')
    print('7 - Exit')

def main():
    ch = 4
    container = MyLinkedList()
    while ch != 7:
        menu()
        ch = int(input('Choice:'))
        if ch == 1:
            number = input_and_check_size()
            container.input_keyboard(number)

        if ch == 2:
            number = input_and_check_size()
            left = input_check_list_element_or_interval_limit()
            right = input_check_list_element_or_interval_limit()
            if left > right:
                temp = left
                left = right
                right = temp
            container.randomize_elements(number, left, right)

        if ch == 3:
            value = input_check_list_element_or_interval_limit()
            index = input_and_check_index(container.get_size())
            container.new_node(value, index)

        if ch == 4:
            if container.get_head() is None:
                print("You can't delete node, because your list is empty")
            else:
                index = input_and_check_index(container.get_size())
                container.delete_node(index)

        if ch == 5:
            print("Result: " + str(container.exercise_count()))

        if ch == 6:
            container.print_list()

        if 7 < ch < 1:
            print('There is no such choice')
            ch = int(input('Choice:'))

if __name__ == '__main__':
    main()