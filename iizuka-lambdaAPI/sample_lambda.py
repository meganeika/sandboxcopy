import json
import random

def lambda_handler(event, context):
    status = ['在宅・離席中','在宅・休憩中','在宅・勤務中']
    num =random.randrange(2)

    if event['color'] != "":
        result = '#'+event['color']
    else:
        result = getDefaultColor()
    return {
        "result": result,
        "name":getName(),
        "color":result,
        "status":status[num]
    }

def getDefaultColor():
    return '#FF0000'

def getName():
    names = ['Yさん','Jさん','Tさん','Iさん','Sさん','Kさん']
    return names[random.randrange(6)]
