import json
from lib.colored import *

def getIndex(li,target):
    for index, x in enumerate(li):
        if x['score'] == target:
            return index
    return -1

def podium(name, score, mode):
    f = open('./scores.json')
    data = json.load(f)
    if mode == '&type=boolean':
        stats = data['stats']['trueFalse']
    else:
        stats = data['stats']['multipleChoice']

    stats.sort(key=lambda x: x['score'], reverse=True)

    podium = '         '+stats[0]['user'][:9] + '\n         █████████         \n         ██╔═══╗██'+stats[1]['user'][:9] +'\n'+stats[2]['user'][:9].zfill(9).replace('0', ' ') + \
             '██║ 1 ║███████████\n███████████╚═══╝████╔═══╗██\n██╔═══╗█████████████║ 2 ║██\n██║ 3 ║█████████████╚═══╝██\n██╚═══╝████████████████████\n███████████████████████████'

    colors = [ '#fc0303', '#fc5e03', '#fcba03', '#98fc03', '#03fc18', '#03e7fc', '#0367fc', '#0303fc', '#c203fc', '#fc037b']     # Easter Egg
    hex = '0123456789abcdef'
    if name == 'lolcat':
        newPodium = ''
        for i in range(len(podium)):
            newPodium += colored(podium[i], colors[i % len(colors)])
        podium = newPodium
    print(podium)

    for i in range(3):
        i = i-1
        if i != 0: color = '#858585'
        else: color = '#ffffff'
        if getIndex(stats, score) + 1 + i < 1: continue
        try:
            print(colored(str(getIndex(stats, score) + 1 + i) + '. | ' + stats[getIndex(stats, score) + i]['user'][:14].zfill(14).replace('0', ' ') + ' | ' + str(stats[getIndex(stats, score) + i]['score']), color))
        except IndexError:
            print('')
    f.close()