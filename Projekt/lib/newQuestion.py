from urllib.request import urlopen
import json


def newQuestion(topic, difficulty, gamemode):
    url = 'https://opentdb.com/api.php?amount=1' + topic + difficulty + gamemode

    response = urlopen(url)
    data = json.loads(response.read())

    return data
