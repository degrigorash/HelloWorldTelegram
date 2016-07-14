# -*- coding: utf-8 -*-
from twx.botapi import TelegramBot

BOT_TOKEN = '261616344:AAG7mO1GEA6KDwPYFV6V3hiXv1PMfKYlcvM'

bot = TelegramBot(BOT_TOKEN)

if __name__ == '__main__':
     a = bot.send_message(u'@helloworldru', u'Hellorld barowold!').wait()
     print(a)