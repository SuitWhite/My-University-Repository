class MyException(Exception):
    pass


def input_positive_number():
    while True:
        try:
            n = int(input())
            if n <= 0:
                raise MyException
            return n
        except MyException:
            print("N<1")
            continue
        except ValueError:
            print("Value should be int")
            continue


def count1(n, m):
    count = 0
    if m > 0 and n - 1 >= 0:
        count += count1(n - 1, m - 1)
    if n - 10 >= 0:
        count += count1(n - 10, 3)
    if n == 0:
        return 1
    return count

def Exit():
    print("Вийти з програми? (y,n):")
    ch = input()
    if (ch=='y'):
        exit()

def main():
    while True:
        print("Введіть розмір конструкції:")
        size = input_positive_number()
        count = count1(size, 3)
        print(f'Результат: {count}')
        Exit()


if __name__ == '__main__':
    main()
