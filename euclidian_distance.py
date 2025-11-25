x = 6
y = 6

h = -6
u = -6

def point1(x, y):
    return (x, y)

def point2(h, u):
    return (h, u)

p1 = point1(x, y)
p2 = point2(h, u)


def absolute(p1, p2):
    x, y = p1
    h, u = p2

    a = abs(x - h)
    b = abs(y - u)

    return a, b


def theorem(a, b):
    c_squared = a*a + b*b
    return c_squared

c_squared = theorem(a, b)

def squarerootc(n):
    return n ** 0.5

a, b = absolute(p1, p2)

c = c_squared ** 0.5

print("Distance is:", c)
