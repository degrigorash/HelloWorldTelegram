# -*- coding: utf-8 -*-
import config
import telebot

BOT_TOKEN = '261616344:AAG7mO1GEA6KDwPYFV6V3hiXv1PMfKYlcvM'

bot = telebot.TeleBot(BOT_TOKEN)

if __name__ == '__main__':
     bot.send_message('@helloworldru', 'Hello World!!!')