from random import choices

def menu():
    while True:
        try:
            n = input('Меню:\n"1" - ввести матрицю для сортування\n'
                      '"2" - згенерувати матрицю для сортування\n'
                      '"exit" - вихід з програми\n')
            if n == 'exit':
                print('програма завершила свою роботу')
                exit()
            elif n == "1":
                return matrix_init()
            elif n == "2":
                return generate_matrix()
            else:
                n = int('error')
                return n
        except ValueError:
            print('Такої опції немає. Спробуйте ще раз\n')
            continue


def input_number():
    while True:
        try:
            n = int(input())
            return n
        except ValueError:
            print("Value should be int")
            continue

def matrix_init():
    print("Enter size")
    a = []
    N = input_number()
    for i in range(N):
        a.append([0]*N)
    for i in range(N):
        for j in range(N):
            a[i][j] = input_number()
    return a


def generate_matrix():
    print("Enter size, a and b:")
    N = input_number()
    matrix = []
    a = input_number()
    b = input_number()
    for i in range(N):
        m = choices(range(a, b), k=N)
        matrix.append(m)

    return matrix

def show_matrix(matrix, size_of_matrix):
    for i in range(size_of_matrix):
        ryadok = ""
        for j in range(size_of_matrix):
            ryadok+=str(matrix[i][j])
            ryadok+=" "
        print(ryadok)


def start(matrix):
    print("Enter key:")
    key = input_number()
    size = len(matrix)
    show_matrix(matrix, size)
    sort_matrix(matrix, key)
    print('Matrix after sorting:')
    show_matrix(matrix, size)



def sort_matrix(matrix, key):
    n = len(matrix)
    temporary_matrix = [0] * (n * n)
    k = 0
    count = 0

    for i in range(0, n):
        for j in range(0, n):
            temporary_matrix[k] = matrix[i][j]
            k += 1
            count += 1

    # sort temp[]
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(temporary_matrix) - 1):
            if temporary_matrix[x] > temporary_matrix[x + 1]:
                # Swap the elements
                temporary_matrix[x], temporary_matrix[x + 1] = temporary_matrix[x + 1], temporary_matrix[x]
                count += 1
                # Set True loop again
                swapped = True
    binary_search(temporary_matrix, 0, len(temporary_matrix) - 1, key)
    # copy the elements of temp[]
    # one by one in mat[][]
    k = 0
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = temporary_matrix[k]
            k += 1
            count += 1

    print(f'\nСортування виконано за {count} операцій\n')


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        matrix = menu()
        if start(matrix) is False:
            print("Element is not found")
        else:
            print("Element is found")
