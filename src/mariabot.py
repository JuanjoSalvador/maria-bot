# -*- coding: utf-8 -*-

import telebot

bot = telebot.TeleBot("226508529:AAFmAlsrMmKRDtLADDAo2SQPD24uM8seoL8")


@bot.message_handler(func=lambda m: True, content_types=['new_chat_members', 'text'])
def welcome(message):
    new_member = message.new_chat_member.username
    msg = "Bienvenido/a a Andalucia Developers, " + new_member + ". Espero que tu estancia sea agradable, y no te olvides de leer las normas del grupo aqui \n\n http://telegra.ph/Normas-del-grupo-Andaluc%C3%ADa-Developers-08-10"
    chat_id = message.chat.id
    
    bot.send_message(chat_id, msg)

bot.polling()