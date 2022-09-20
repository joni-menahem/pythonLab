import telebot
import time
from intervalSelector import EveryXMin

API_KEY = '5552412386:AAFG4PoSOIKInCeI8yyorD44zlHbt4Wgcxw'
bot = telebot.TeleBot(API_KEY)
Reminder = True
Minute = 0.1 # time in seconds for one minute (for testing purposes)

# Instruction for first time use when user press 'start'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, \n\nYou're probably here because you tend to forget to drink. \n\nIf you wish to get a water drinking reminder, please select: /remindme")

# Send a reminder
@bot.message_handler(commands=['remindme'])
def remindme(message):
  global Reminder
  Reminder = True
  bot.send_message(message.chat.id, "Please choose the reminder interval: \n\nRemind me every 45 minutes: /remind45 \n\nRemind me every 60 minutes: /remind60 \n\nRemind me every 75 minutes: /remind75 \n\nRemind me every 90 minutes: /remind90 \n\n\n To disable the auto timer: /stop")

# Send a reminder for 45 mins
@bot.message_handler(commands=['remind45'])
def remind45(message):
  while Reminder == True:
    sendmessage = bot.send_message(message.chat.id, EveryXMin(45) + "\n\nYou can stop at any time by selecting /stop")
    sendmessage
    time.sleep(45*Minute)

# Send a reminder for 60 mins
@bot.message_handler(commands=['remind60'])
def remind60(message):
  while Reminder == True:
    sendmessage = bot.send_message(message.chat.id, EveryXMin(60) + "\n\nYou can stop at any time by selecting /stop")
    sendmessage
    time.sleep(60*Minute)

# Send a reminder for 75 mins
@bot.message_handler(commands=['remind75'])
def remind75(message):
  while Reminder == True:
    sendmessage = bot.send_message(message.chat.id, EveryXMin(75) + "\n\nYou can stop at any time by selecting /stop")
    sendmessage
    time.sleep(75*Minute)

# Send a reminder for 90 mins
@bot.message_handler(commands=['remind90'])
def remind90(message):
  while Reminder == True:
    sendmessage = bot.send_message(message.chat.id, EveryXMin(90) + "\n\nYou can stop at any time by selecting /stop")
    sendmessage
    time.sleep(90*Minute)

@bot.message_handler(commands=['stop'])
def stop(message):
  global Reminder
  Reminder = False
  bot.send_message(message.chat.id, 'Reminder stopped.')
  time.sleep(1)
  bot.send_message(message.chat.id, "If you wish to get a water drinking reminder again, please select: /remindme")



# Handles all messages which text matches the regex regexp.
# See https://en.wikipedia.org/wiki/Regular_expression
# This regex matches all sent url's.
@bot.message_handler(regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
def command_url(message):
    bot.reply_to(message, "I shouldn't open that url, should I?")

bot.polling(none_stop=True)