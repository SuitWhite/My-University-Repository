def fac(n):
    if (n == 0 or n<1):
        return 1
    return fac(n-1) * n

class MyException(Exception): pass
while True:
        try:
            print("Enter k:")
            k = int(input())
            if k<=0:
                raise MyException
            result = fac(k//10)*fac(k%10)
            print("For k you have ", result, "variants")
        except MyException:
            print("k<1")
            continue
        except ValueError:
            print("Value should be int")
            continue
