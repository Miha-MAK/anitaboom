import telebot
from telebot import types
from time import sleep
from datetime import datetime
import pytz


bot = telebot.TeleBot("1208171110:AAFlG9fAhQOeldF_N2HhBvyfHOREbnXFLCU")

with open("adresses.txt", "r") as f:
    chat_for = [line.rstrip('\n') for line in f]
    print(chat_for)
#@test_test_43_bot
#https://t.me/firechannel1
print("start")
@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button_yes = types.InlineKeyboardButton(text="Да, конечно✅", callback_data=f"yes{message.from_user.id}")
    callback_button_no = types.InlineKeyboardButton(text="Нет, не сейчас❎", callback_data="no")
    keyboard.add(callback_button_yes, callback_button_no)
    bot.send_message(message.chat.id, """Добро пожаловать {}!🙋‍♂️
Я являюсь ботом канала «🔥MAK-S ГОРЯЩАЯ РЕКЛАМА🔥».
Хотите ли Вы что то опубликировать на канале?""".format(message.from_user.first_name), reply_markup=keyboard)

ls = []

@bot.message_handler(content_types = ['text'])
def reply_msg(message):

    ls.append(message.text)

    print(ls)

    bot.send_message(message.chat.id, text = """Таймер поставлен ⏳...сообщения будут отправляться в
{}, теперь напишите текст поста""".format(ls[-1]))

    while True:
        if datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M") in ls:
            tz = pytz.timezone('Asia/Yerevan')

            print("yeeeee")
            ls.pop(0)
            for name in chat_for:
                bot.send_message(name, ls[-1], message.message_id)
            print(ls)
            ls.clear()
            print(ls)
            bot.send_message(message.chat.id, text = "Сообщения успешно отправлены✅")

            break

        sleep(60)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data.startswith("yes"):
        #bot.send_message(call.message.chat.id, text = "Хорошо, напишите текст ( Можете использовать ссылки, емодзи, и т.д )")
        global ID
        ID = str(call.data.replace("yes","")) # ID клиента

        s = bot.send_message(call.message.chat.id, text = "Напишите дата и время в таком формате:\n2020-06-18 16:50...📝")

        bot.register_next_step_handler(s,reply_msg) # Переходим в reply_msg


    elif call.data == "no":
        bot.send_message(call.message, text = "Хорошо, если передумаете - напишите, я всегда тут!🤖")


bot.polling()
