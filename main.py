from random import random
def getInputs():
    probA = float(input("请输入选手A的能力值(0-1)："))
    probB = float(input("请输入选手B的能力值(0-1)："))
    return probA, probB
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = 'A'
    i = 1
    while not gameOver(scoreA, scoreB):
        serving = switchServing(i, serving)
        i += 1
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
        else:
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1
    print(scoreA, '---', scoreB)
    return Winner(scoreA, scoreB)
def gameOver(scoreA, scoreB):
    return (max(scoreA, scoreB) == 11 and abs(scoreA - scoreB) >= 2) or \
           (max(scoreA, scoreB) == 12 and abs(scoreA - scoreB) == 2)
def switchServing(i, serving):
    if i % 2 == 0 and i > 0:
        if serving == 'A':
            serving = 'B'
        else:
            serving = 'A'
    return serving
def Winner(scoreA, scoreB):
    if scoreA ==12 or scoreB == 12:
        if scoreA == 12:
            return 'A'
        else:
            return 'B'
    else:
        if scoreA == 11:
            return 'A'
        else:
            return 'B'
def simOneChampion():
    A, B, round = 0, 0, 1
    probA, probB = getInputs()
    while True:
        print('第{}局'.format(round))
        r = simOneGame(probA, probB)
        round += 1
        if r == 'A':
            A += 1
        else:
            B += 1
        if A == 2:
            print('A获胜')
            break
        elif B == 2:
            print('B获胜')
            break
        else:
            continue
simOneChampion()
