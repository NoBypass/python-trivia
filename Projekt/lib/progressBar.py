import math

def progressBar(percentage, width):
    x = '█' * math.floor(width / 100 * percentage)
    y = '░' * (width - math.floor(width / 100 * percentage))
    #return colored('❰' + x, getColor(percentage)) + colored(y + '❱', getColor(percentage))
    return '❰' + x + y + '❱'