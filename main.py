def fac(n):
    if (n == 0 or n<1):
        return 1
    return fac(n-1) * n
print("Enter k:")
k = int(input())
result = fac(k//10)*fac(k%10)
print("For k you have ", result, "variants")