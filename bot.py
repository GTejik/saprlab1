import telebot
import time

token = '186579531:AAHAX0mPa7AJi0GVCgcFitxbODV46Xu-kmg'


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            bot.send_message(m.chat.id, m.text)


if __name__ == '__main__':
    bot = telebot.TeleBot(token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
