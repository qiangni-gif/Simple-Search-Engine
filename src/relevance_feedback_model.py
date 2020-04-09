import json
UOfeedback = '../output/UOfeedback.json'
reuterfeedback = '../output/reuterfeedback.json'

def reset():
    feedback = {}
    with open(UOfeedback,'w') as U:
        json.dump(feedback, U, sort_keys=True, indent=4,ensure_ascii=False)
    with open(reuterfeedback,'w') as R:
        json.dump(feedback, R, sort_keys=True, indent=4,ensure_ascii=False)

def loadfb(collection):
    if collection == "UofO catalog":
        path = UOfeedback
    else:
        path = reuterfeedback
    with open(path, 'r') as fd:
        return json.load(fd)

def savefb(feedback,collection):
    if collection == "UofO catalog":
        path = UOfeedback
    else:
        path = reuterfeedback
    with open(path, 'w') as fd:
        json.dump(feedback, fd, sort_keys=True, indent=4,ensure_ascii=False)

def setfd(feedback,collection,bool):
    fb = loadfb(collection)
    if bool:
        if feedback[0] not in fb:
            fb[feedback[0]] = {'relevant':[],'not relevant':[]}
            fb[feedback[0]]['relevant'].append(feedback[1])
        else:
            fb[feedback[0]]['relevant'].append(feedback[1])
            if feedback[1] in fb[feedback[0]]['not relevant']:
                fb[feedback[0]]['not relevant'].remove(feedback[1])
    else:
        if feedback[0] not in fb:
            fb[feedback[0]] = {'relevant':[],'not relevant':[]}
            fb[feedback[0]]['not relevant'].append(feedback[1])
        else:
            fb[feedback[0]]['not relevant'].append(feedback[1])
            if feedback[1] in fb[feedback[0]]['relevant']:
                fb[feedback[0]]['relevant'].remove(feedback[1])

    savefb(fb,collection)

reset()