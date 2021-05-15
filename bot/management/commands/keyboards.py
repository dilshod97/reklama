from telegram import KeyboardButton, ReplyKeyboardMarkup
import math


def darslar(darslar):
    keyboard = []
    for reg in darslar:
        keyboard += [[KeyboardButton(reg.name)]]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    return reply_markup











