import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)

default_rarity = 0
rare_rarity = 0    
rare_plus_rarity = 0
legendary_rarity = 0
legendary_plus_rarity = 0

sell_cards = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    # sti = open('static/welcome.webp' , 'rb')
    # bot.send_sticker(message.chat.id, sti)
    # keyboard

    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("Добыть 💸")
    item2 = types.KeyboardButton("Профиль 📁")
    item3 = types.KeyboardButton("Рандомный Поззи 🎲")
 
    markup.add(item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать,\nЯ, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

BALANCE = 50       

# STATE = {
#     # <user_id_1>: <value>,
#     # <user_id_2>: <value>,
#     #   .
#     #   .
#     #   .
#     # <user_id_N>: <value>
# }

@bot.message_handler(content_types=['text'])
def Default_case(message): 
    global BALANCE
    
    if message.chat.type == 'private':
        global BALANCE
        global default_rarity
        global rare_rarity
        global rare_plus_rarity
        global legendary_rarity 
        global legendary_plus_rarity
        
        if message.text == "Рандомный Поззи 🎲":
            if BALANCE > 5 :
                chanse = int(random.randint(0,1000))
                BALANCE -= 5
                bal_m ="На вашем балансе осталось: " + str(BALANCE) + " $"

                if chanse > 0 and chanse <= 500:
                    default_rarity += 1
                    bot.send_message(message.chat.id,  str(bal_m) + "\nВам выпала карта" + "\nРедкость: дефолтная\n" + "\nCейчас у вас: " + str(default_rarity) + " таких карт")
                    
                elif chanse > 500 and chanse <= 700:
                    rare_rarity += 1
                    bot.send_message(message.chat.id, str(bal_m) + "\nВам выпала карта" + "\nРедкость: редкая" + "\nCейчас у вас: " + str(rare_rarity) + " таких карт")

                elif chanse > 700 and chanse <= 800:
                    rare_plus_rarity += 1
                    bot.send_message(message.chat.id, str(bal_m) + "\nВам выпала карта" + "\nРедкость: редкая+" + "\nCейчас у вас: " + str(rare_plus_rarity) + " таких карт")

                elif chanse > 800 and chanse <= 810:
                    legendary_rarity += 1
                    bot.send_message(message.chat.id, str(bal_m) + "\nВам выпала карта" + "\nРедкость: легендарная" + "\nCейчас у вас: " + str(legendary_rarity) + " таких карт")

                elif chanse > 810 and chanse <= 811:
                    legendary_plus_rarity += 1
                    bot.send_message(message.chat.id, str(bal_m) + "\nВам выпала карта" + "\nРедкость: легендарная+" + "\nCейчас у вас: " + str(legendary_plus_rarity) + " таких карт" )

                else:
                    bot.send_message(message.chat.id, 'Ничего не выпало')
            else:
                bot.send_message(message.chat.id, 'Недостаточно денег')
        elif message.text == 'Профиль 📁':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Инвентарь", callback_data='inventory')
            item2 = types.InlineKeyboardButton("Баланс", callback_data='balance')
            item3 = types.InlineKeyboardButton("Продажа", callback_data='sell')
 
            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, 'Ваш Профиль', reply_markup=markup)
        elif message.text == "Добыть 💸":
            BALANCE_plus_chanse = int(random.randint(1,5))
            if BALANCE_plus_chanse == 1:
                BALANCE += 1
                bot.send_message(message.chat.id, "Вам выпал 1 $")
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
                    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global sell_cards
    global default_rarity
    global rare_rarity
    global rare_plus_rarity
    global legendary_rarity 
    global legendary_plus_rarity
    global BALANCE
    default = 1
    rare = 10
    rare_plus = 50
    legendary = 100
    legendary_plus = 500
       
    try:
        if call.message:
            if call.data == 'inventory':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Инвентарь",
                reply_markup=None)
                bot.send_message(call.message.chat.id, "Карты:\n" + "" + "\nДефолтные : " + str(default_rarity) + "\nРедкие : " + str(rare_rarity) + "\nРедкие+ : " + str(rare_plus_rarity) + "\nЛегендарные : " + str(legendary_rarity) + "\nЛегендарные+ : " + str(legendary_plus_rarity))
                            
            elif call.data == 'balance':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Баланс",
                reply_markup=None)
                bot.send_message(call.message.chat.id, "На вашем балансе осталось: " + str(BALANCE) + " $")
                
                
            elif call.data == 'sell':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Карты", callback_data='cards')
                item2 = types.InlineKeyboardButton("Другое", callback_data='other')
 
                markup.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Продажа",
                reply_markup=markup)

            elif call.data == 'cards':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Дефолтные", callback_data='default')
                item2 = types.InlineKeyboardButton("Редкие", callback_data='rare')
                item3 = types.InlineKeyboardButton("Редкие+", callback_data='rare+')
                item4 = types.InlineKeyboardButton("Легендарные", callback_data='legendary')
                item5 = types.InlineKeyboardButton("Легендарные+", callback_data='legendary+')
            
                markup.add(item1, item2, item3, item4, item5)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какую Редкость Вы хотите продать?",
                reply_markup=markup)
            
            elif call.data == 'default':
                trade = 0
                accept = 0
                cancel = 0
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("+ 1", callback_data='plus_1')
                item2 = types.InlineKeyboardButton("+50", callback_data='plus_50')
                item3 = types.InlineKeyboardButton("Продать всё", callback_data='sell_all')
                item4 = types.InlineKeyboardButton("- 1", callback_data='minus_1')
                item5 = types.InlineKeyboardButton("Подтвердить", callback_data='accept')
                item6 = types.InlineKeyboardButton("Отменить", callback_data='cancel')

                markup.add(item1, item2, item3, item4, item5, item6)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите кол-во, и продайте вещь",
                reply_markup=markup)
                while sell_cards < default_rarity and trade != 1:
                    # bot.send_message(call.message.chat.id, "работает")
                    if call.data == "plus_1":
                        sell_cards += 1
                        bot.send_message(call.message.chat.id, sell_cards)

                    elif call.data == "plus_50":
                        sell_cards += 50
                        bot.send_message(call.message.chat.id, sell_cards)
                        
                    elif call.data == "sell_all":
                        sell_cards = default_rarity                        
                        bot.send_message(call.message.chat.id, sell_cards)
                        
                    elif call.data == "minus_1":
                        sell_cards -= 1
                    
                    elif call.data == "accept":                       
                        BALANCE += sell_cards * default
                        default_rarity -= sell_cards
                        sell_cards = 0
                        trade = 1
                        
                    elif call.data == "cancel":
                        
                        markup = types.InlineKeyboardMarkup(row_width=1)
                        item1 = types.InlineKeyboardButton("Дефолтные", callback_data='default')
                        item2 = types.InlineKeyboardButton("Редкие", callback_data='rare')
                        item3 = types.InlineKeyboardButton("Редкие+", callback_data='rare+')
                        item4 = types.InlineKeyboardButton("Легендарные", callback_data='legendary')
                        item5 = types.InlineKeyboardButton("Легендарные+", callback_data='legendary+')               
                        markup.add(item1, item2, item3, item4, item5)
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какую Редкость Вы хотите продать?",
                        reply_markup=markup)
                        sell_cards = 0
                        trade = 1
            # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            # text="Крііііінж")
    except Exception as e:
        print(repr(e))
# RUN
bot.polling(none_stop=True)