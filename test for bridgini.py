import random


def getLooserName(score, names):
    maxScore = max(score)
    looser = []
    for i in range(len(score)):
        if score[i] == maxScore:
            looser.append(names[i])
    if len(looser) == 1:
        return looser[0]
    else:
        index = random.randint(0, len(looser)-1)
        return looser[index]


names = ['Dor', 'Liran', 'Yoni', 'Ido']
score = [9, 0, 0, 9]

print(getLooserName(score, names))
