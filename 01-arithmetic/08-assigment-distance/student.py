# write your code here
from math import sqrt
def distance(x1, y1, x2, y2):
    x = (x2-x1)**2
    y = (y2-y1)**2
    return sqrt(x+y)