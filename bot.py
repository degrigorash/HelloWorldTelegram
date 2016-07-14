# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # �������� ������� �� ������ ������� ����, � ��������
    bot.sendMessage(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)