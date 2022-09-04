import random
import pandas as pd

messages = pd.read_csv('messages.txt', sep='\t', header=None, index_col=False)
messages.columns = ['message']

def GetRandomMessage(info):
    rnd = random.randint(0, messages.shape[0]-1)
    temp = messages.at[rnd,'message']
    message = temp  + '\n' + 'Recommended dose: 200ml' + '\n\n' + 'The next reminder will be in' + ' ' + info
    return message

def EveryXMin(time):
    time = str(time)
    info = time + " " + "minutes"
    message = GetRandomMessage(info)
    return message

def Every60Min():
    info = "60 minutes"
    message = GetRandomMessage(info)
    return message

def Every50Min():
    info = "50 minutes"
    message = GetRandomMessage(info)
    return message

def Every45Min():
    info = "45 minutes"
    message = GetRandomMessage(info)
    return message

def Every40Min():
    info = "40 minutes"
    message = GetRandomMessage(info)
    return message

def Every30Min():
    info = "30 minutes"
    message = GetRandomMessage(info)
    return message

def Every20Min():
    info = "20 minutes"
    message = GetRandomMessage(info)
    return message

def Every15Min():
    info = "15 minutes"
    message = GetRandomMessage(info)
    return message