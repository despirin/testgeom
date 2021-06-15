
from geom2d.point import *

#l = [Point(i, i*i) for i in range (-5, 6)]

l = list(map(lambda i: Point (i, i*i), range (-5, 6)))
#
# for el in l:
#     el.y = -el.y

print(l)

