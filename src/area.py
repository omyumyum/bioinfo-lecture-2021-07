import math


def area(r):
    return(r**2 * math.pi)

area_input = int(input('입력: '))
print(area(area_input))
