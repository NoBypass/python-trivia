import math


def progressBar(percentage, width):
    x = '█' * math.floor(width / 100 * percentage)
    y = '░' * (width - math.floor(width / 100 * percentage))
    return '❰' + x + y + '❱'
