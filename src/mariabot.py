# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot(<TOKEN>)

@bot.message_handler(commands=['repo'])
def repository(message):
    bot.reply_to("Repositorio de Maria disponible en GitHub https://github.com/JuanjoSalvador/maria-bot")

@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def welcome(message):
    new_member = message.new_chat_member.username
    msg = <YOUR WELCOME MESSAGE HERE>
    chat_id = message.chat.id
    
    bot.send_message(chat_id, msg)

bot.polling()
