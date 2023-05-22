import json


def to_scores(data, mode):
    scores_json = open('./scores.json')

    json_object = json.load(scores_json)

    if mode == '&type=boolean':
        json_object['stats']['trueFalse'].append(data)
    else:
        json_object['stats']['multipleChoice'].append(data)

    scores_json.close()
    with open('scores.json', 'w') as f:
        json.dump(json_object, f)
