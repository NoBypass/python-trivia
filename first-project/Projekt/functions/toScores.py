import json

def toScores(data, mode):
    scoresJSON = open('./scores.json')

    JSONobject = json.load(scoresJSON)

    if mode == '&type=boolean':
        JSONobject['stats']['trueFalse'].append(data)
    else:
        JSONobject['stats']['multipleChoice'].append(data)

    scoresJSON.close()
    with open('scores.json', 'w') as f:
        json.dump(JSONobject, f)