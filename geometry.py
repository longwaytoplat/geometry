from geom2d.point import *

l1 = [Point(2, 1), Point(0, 0), Point(1, 2)]


def x(p):
    return p.x


def y(p):
    return p.y


l2 = sorted(l1, key=y)

print(l1)
print(l2)
