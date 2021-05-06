import random
import noise
import math


def get(request):
    radius = request.args.get('radius')

    # generate everything except the poles
    width = 2*math.pi*radius
    height = width // 2

    heightmap = []

    for x in range(0, width):
        for y in range(0, height):
            heightmap[x*height +
                      y] = noise.pnoise2(1/x, 1/y, repeatx=width, repeaty=height)

    return ''
