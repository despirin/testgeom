from geom2d.point import *

# a = Point(0, 0)
# b = Point(3, 4)
# print (a.dist(b))
# print(a == b)
# print(a == Point(0, 0))

l1 = [Point(0, 0), Point(2, 1), Point(1, 2)]
# l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
# l2 = list(l1)
# l2[0] = Point(0,0)

# def x(p):
#     return p.x
# def y(p):
#     return p.y

l2 = sorted(l1, key=lambda p: p.x)
l2 = sorted(l1, key=lambda p: p.dist(Point(0, 0)))

print (l1)
print (l2)