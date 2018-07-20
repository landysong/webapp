def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'


def triangles():
    ls = [1]
    while True:
        yield ls
        ls = [1] + [ls[i] + ls[i+1] for i in range(len(ls) - 1)] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
