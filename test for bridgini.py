import random
score = {"r1": 1, "r2": 1, "r3": 1, "r4": 1, "r5": 1, "r6": 1, "r7": 1, "r8": 1, "r9": 5, "r10": 1,
         "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "b9": 3, "b10": 0,
         "o1": 0, "o2": 0, "o3": 0, "o4": 0, "o5": 0, "o6": 0, "o7": 0, "o8": 0, "o9": 3, "o10": 0,
         "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "g9": 3, "g10": 0}

deck = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
        "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
        "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
        "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]


def rotateList(list, x):
    return list[-x % len(list):] + list[:-x % len(list)]


names = ['dor', 'liran', 'yoni', 'ido', 'daniel']
print('names:', names)
whoLost = random.choice(names)
print('wholost', whoLost)
rotate = names.index(whoLost)
print('index in list', rotate)
new = rotateList(names, -rotate)
print('list after rotation', new)
