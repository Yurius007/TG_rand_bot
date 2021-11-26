import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
global BALANCE
BALANCE = 100


@bot.message_handler(commands=['start'])
def welcome(message):
 
    # keyboard

    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("🎲 Открыть Ящик")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("🎲 Рандомный Поззи")
 
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать,\nЯ, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def Default_case(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомный Поззи':
            chanse = int(random.randint(0,1000))
            BALANCE + 5
            bal_m ="На вашем балансе осталось: " + str(BALANCE) + " $"

            if chanse > 0 and chanse <= 500:
                bot.send_message(message.chat.id, str(chanse) + "\nРедкость: дефолтная" + "\n" + bal_m)

            elif chanse > 500 and chanse <= 700:
                bot.send_message(message.chat.id, str(chanse) + "\nРедкость: редкая" + "\n" + bal_m)

            elif chanse > 700 and chanse <= 800:
                bot.send_message(message.chat.id, str(chanse) + "\nРедкость: редкая+" + "\n" + bal_m)

            elif chanse > 800 and chanse <= 810:
                bot.send_message(message.chat.id, str(chanse) + "\nРедкость: легендарная" + "\n" + bal_m)

            elif chanse > 810 and chanse <= 811:
                bot.send_message(message.chat.id, str(chanse) + "\nРедкость: легендарная+" + "\n" + bal_m)

            else:
                bot.send_message(message.chat.id, 'Ничего не выпало')
        elif message.text == '😊 Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("#", callback_data='good')
            item2 = types.InlineKeyboardButton("#", callback_data='bad')
            item3 = types.InlineKeyboardButton("#", callback_data='notsure')
 
            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, '#', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, '#')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, '#')
            elif call.data == 'notsure':
                bot.send_message(call.message.chat.id, '#')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Крііііінж")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)