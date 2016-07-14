# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

if __name__ == '__main__':
     bot.send_message('@helloworldru', 'Hello World!!!')