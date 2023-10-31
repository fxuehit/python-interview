#initial script
def fibonacci(n):
    if n <= 0:
        return "N should be a positive integer"
    elif n == 1:
        return [1]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

#1 get Nth
# O（1）
# this is not o(1), since you have to call fibonnaci first, which is a o(N)
def getn_fibonacci(n):
    fib = fibonacci(n)
    fib_n = fib[n -1]
    return fib_n

#2 get Nth
# O(N)
def get_nth_fibonacci_number(n):
    if n <= 0:
        return "N should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return b

n = 10
#same answer
print(fibonacci(n))
print(getn_fibonacci(n))
print(get_nth_fibonacci_number(n))



