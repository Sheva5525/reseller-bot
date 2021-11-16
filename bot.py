import telebot
import telo, os
from telebot import types
import sqlite3
from telebot.apihelper import ApiTelegramException
import pdf

def is_subscribed(chat_member):
    print(chat_member)
    if chat_member != 'left':
        return True
    else:
        return False

outwear = ["куртка", "ветровка", "пальто"]
midh = ["свитер", "джемпер" , "свитшот", "худи"]
midl = ["футболка", "майка", "компресионное белье"]
bottom = ["Брюки", "Шорты", "Джинсы", "Штаны"]
accessories = ["Очки", "Галстук", "Перчатки", "Шапка", "Кепка"]
bag = ["Портфель", "Сумка"]
cloths = [outwear, midh, midl, bottom, accessories, bag]

markup = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Верх', callback_data=1)
b = telebot.types.InlineKeyboardButton(text='Низ', callback_data=2)
c = telebot.types.InlineKeyboardButton(text='Обувь', callback_data=3)
d = telebot.types.InlineKeyboardButton(text='Сумки', callback_data=4)
markup.row(a, b, c, d)
a = telebot.types.InlineKeyboardButton(text='Аксессуары', callback_data=5)
b = telebot.types.InlineKeyboardButton(text='Разное', callback_data="X")
markup.row(a, b)

markup1 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Куртки', callback_data=11)
b = telebot.types.InlineKeyboardButton(text='Ветровки', callback_data=12)
c = telebot.types.InlineKeyboardButton(text='Пальто', callback_data=13)
markup1.row(a, b, c)
a = telebot.types.InlineKeyboardButton(text='Плащи', callback_data=14)
b = telebot.types.InlineKeyboardButton(text='Жилет', callback_data=321)
markup1.row(a, b)
markup1.add(telebot.types.InlineKeyboardButton(text='Компрессионное бельё', callback_data=110))
b = telebot.types.InlineKeyboardButton(text='Футболки', callback_data=15)
c = telebot.types.InlineKeyboardButton(text='Майки', callback_data=16)
markup1.row(a, b)
a = telebot.types.InlineKeyboardButton(text='Свитера', callback_data=17)
b = telebot.types.InlineKeyboardButton(text='Худи', callback_data=18)
c = telebot.types.InlineKeyboardButton(text='Свитшот', callback_data=19)
markup1.row(a, b, c)
markup1.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))

markup2 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Джинсы', callback_data=21)
b = telebot.types.InlineKeyboardButton(text='Брюки', callback_data=22)
markup2.row(a, b)
a = telebot.types.InlineKeyboardButton(text='Шорты', callback_data=23)
b = telebot.types.InlineKeyboardButton(text='Штаны', callback_data=24)
markup2.row(a, b)
markup2.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))

markup3 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Летняя обувь', callback_data=31)
b = telebot.types.InlineKeyboardButton(text='Зимняя обвуь', callback_data=33)
markup3.row(a, b)
markup3.add(telebot.types.InlineKeyboardButton(text='Осенняя и весенняя обувь', callback_data=32))
markup3.add(telebot.types.InlineKeyboardButton(text='Демисезонная обувь', callback_data=34))
markup3.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))

markup4 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Портфели', callback_data=41)
b = telebot.types.InlineKeyboardButton(text='Сумки', callback_data=42)
markup4.row(a, b)
markup4.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))

markup5 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Очки', callback_data=51)
b = telebot.types.InlineKeyboardButton(text='Галстуки', callback_data=52)
c = telebot.types.InlineKeyboardButton(text='Перчатки', callback_data=53)
markup5.row(a, b, c)
a = telebot.types.InlineKeyboardButton(text='Носки', callback_data=54)
b = telebot.types.InlineKeyboardButton(text='Шапки', callback_data=55)
markup5.row(a, b)
a = telebot.types.InlineKeyboardButton(text='Часы', callback_data=56)
b = telebot.types.InlineKeyboardButton(text='Кепки', callback_data=57)
c = telebot.types.InlineKeyboardButton(text='Платки', callback_data=58)
markup5.row(a, b, c)
markup5.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))

nline = (markup, markup1, markup2, markup3, markup4, markup5)

typecc = [outwear, midh, midl, bottom, accessories, bag]
typec_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

for i in typecc:
    for j in i:
        button = types.KeyboardButton(text=j)
        typec_kb.add(button)

size_list = ["XXS", "XS", "S", "M", "L", "XL", "XXL", "XXXL"]

size_niz = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = types.KeyboardButton(text="W30 L32")
button_2 = types.KeyboardButton(text="W32 L34")
button_3 = types.KeyboardButton(text="W34 L34")
button_4 = types.KeyboardButton(text="W36 L34")
button_5 = types.KeyboardButton(text="W38 L34")
button_6 = types.KeyboardButton(text="W40 L34")
size_niz.row(button_1, button_2, button_3)
size_niz.row(button_4, button_5, button_6)

size_obv = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = types.KeyboardButton(text="37.5 (US 6.5)")
button_2 = types.KeyboardButton(text="38 (US 7)")
button_3 = types.KeyboardButton(text="39 (US 7.5)")
button_4 = types.KeyboardButton(text="39.5 (US 8)")
button_5 = types.KeyboardButton(text="40 (US 8.5)")
button_6 = types.KeyboardButton(text="41 (US 9)")
button_7 = types.KeyboardButton(text="41.5 (US 9.5)")
button_8 = types.KeyboardButton(text="42 (US 10)")
button_9 = types.KeyboardButton(text="43 (US 10.5)")
button_10 = types.KeyboardButton(text="43.5 (US 11)")
button_11 = types.KeyboardButton(text="44 (US 11.5)")
button_12 = types.KeyboardButton(text="44.5 (US 12)")
button_13 = types.KeyboardButton(text="45 (US 12.5)")
button_14 = types.KeyboardButton(text="46 (US 13)")
button_15 = types.KeyboardButton(text="47 (US 13.5)")
size_obv.row(button_1, button_2)
size_obv.row(button_3, button_4)
size_obv.row(button_5, button_6)
size_obv.row(button_7, button_8)
size_obv.add(button_9)
size_obv.row(button_10, button_11)
size_obv.row(button_12, button_13)
size_obv.row(button_14, button_15)


bot = telebot.TeleBot("2122350628:AAFQKAUoL6Xr6RLz8OMZ31rMaCmJy_p31rE", parse_mode=None)
user = {}
size_keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = types.KeyboardButton(text="XXS")
button_2 = types.KeyboardButton(text="XS")
button_3 = types.KeyboardButton(text="S")
button_4 = types.KeyboardButton(text="M")
button_5 = types.KeyboardButton(text="L")
button_6 = types.KeyboardButton(text="XL")
button_7 = types.KeyboardButton(text="XXL")
button_8 = types.KeyboardButton(text="XXXL")
size_keyb.row(button_1, button_2)
size_keyb.row(button_3, button_4, button_5)
size_keyb.row(button_6, button_7, button_8)

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = types.KeyboardButton(text="Добавить товар")
button_2 = types.KeyboardButton(text="Посмотреть мой профиль")
button_3 = types.KeyboardButton(text="Изменить данные")
button_4 = types.KeyboardButton(text="Удалить вещь")
kb.add(button_1)
kb.add(button_2)
kb.add(button_3)
kb.add(button_4)

def redact(message):
    kbb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_11 = types.KeyboardButton(text="Изменить имя")
    button_22 = types.KeyboardButton(text="Изменить контакты")
    button_33 = types.KeyboardButton(text="Изменить общую информацию")
    kbb.add(button_11)
    kbb.add(button_22)
    kbb.add(button_33)
    bot.send_message(message.chat.id, "Что именно ты хочешь изменить?", reply_markup=kbb)
    

def full_redact(message, ids, remow):
    message1 = message
    ids = str(ids)
    message = message.text
    if remow == "Изменить имя":
            sqlite_connection = sqlite3.connect('sallers.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(f"""UPDATE sallers SET name = ?
                            where id = ?""",[message, ids])
            sqlite_connection.commit()
            cursor.close()
    if remow == "Изменить контакты":
            sqlite_connection = sqlite3.connect('sallers.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(f"""UPDATE sallers SET contacts = ?
                            where id = ?""",[message, ids])
            sqlite_connection.commit()
            cursor.close()
    if remow == "Изменить общую информацию":
            sqlite_connection = sqlite3.connect('sallers.db')
            cursor = sqlite_connection.cursor()
            cursor.execute(f"""UPDATE sallers SET inf = ?
                            where id = ?""",[message, ids])
            sqlite_connection.commit()
            cursor.close()
    bot.send_message(message1.chat.id, "Твои данные изменены", reply_markup=kb)
    
def show_me(message):
    ids = str(message.from_user.id)
    if (not os.path.exists(str(ids))):
        return bot.send_message(message.chat.id, "Тебя нет в базе данных продавцов. Напиши 'Создать аккаунт', чтоб добавить себя в базу данных")
    else:
        pass
    sqlite_connection = sqlite3.connect('sallers.db')
    cursor = sqlite_connection.cursor()
    count = list(cursor.execute(f"""SELECT * FROM sallers
                                where id = {ids}"""))
    sqlite_connection.commit()
    cursor.close()
    bot.send_message(message.chat.id, "Твой id: " + count[0][0] + "\nТвоё имя: " + count[0][1] + "\nТвои контакты: " + count[0][2] + "\nОбщая информация о тебе: " + count[0][3])
    

@bot.message_handler(commands=['add_saller'])
def add_new_saller(message):
    ids = message.from_user.id
    user[str(ids)] = [str(ids)]
    if (not os.path.exists(str(ids))):
        pass
    else:
        return bot.send_message(message.chat.id, "Ты уже есть в базе данных")
    msg = bot.reply_to(message, "Придётся немного ввести текст. Как тебя звать?", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, add_name)
    #add_saller()

def add_name(message):
    ids = message.from_user.id
    user[str(ids)].append(message.text)
    message = bot.reply_to(message, 'Введи контакты')
    bot.register_next_step_handler(message, add_contacts)
def add_contacts(message):
    ids = message.from_user.id
    user[str(ids)].append(message.text)
    message = bot.reply_to(message, 'Введи общую информацию')
    bot.register_next_step_handler(message, add_inf)
def add_inf(message):
    ids = message.from_user.id
    bot.send_message(message.chat.id, "Я добавил тебя в базу данных", reply_markup=kb)
    user[str(ids)].append(message.text)
    add(ids)

def add(ids):
    ids = str(ids)
    telo.add_saller(user[ids][0], user[ids][1], user[ids][2], user[ids][3])
    
@bot.message_handler(commands=['start'])
def start(message):
    ids = message.from_user.id
    if not is_subscribed(bot.get_chat_member(chat_id="@reseller_news", user_id=ids).status):
        link = f"https://t.me/reseller_news"
        bot.send_message(message.chat.id, f'Чтоб пользоваться ботом, подпишись на наш канал:\n' + link)
        return 0
    if not os.path.exists(str(ids)):
        pass
    else:
        return bot.send_message(message.chat.id, "Я тебя снова приветствую", reply_markup=kb)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Создать аккаунт")
    keyboard.add(button_1)
    bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def foo(message: types.Message):
    ids = message.from_user.id
    if not is_subscribed(bot.get_chat_member(chat_id="@reseller_news", user_id=ids).status):
        link = f"https://t.me/reseller_news"
        bot.send_message(message.chat.id, f'Чтоб пользоваться ботом, подпишись на наш канал:\n' + link)
        return 0
    if message.text == "Создать аккаунт":
        add_new_saller(message)
    if message.text == "Посмотреть мой профиль":
        show_me(message)
        bot.send_document(message.chat.id, open(pdf.show_prof(str(message.from_user.id)), "rb"))
    if message.text == "Изменить данные":
        ids = message.from_user.id
        if (not os.path.exists(str(ids))):
            return bot.send_message(message.chat.id, "Тебя нет в базе данных продавцов. Напиши 'Создать аккаунт', чтоб добавить себя в базу данных")
        else:
            pass
        redact(message)
    if message.text == "Изменить имя":
        ids = message.from_user.id
        message = bot.reply_to(message, 'Введи новое имя')
        bot.register_next_step_handler(message, full_redact, ids, "Изменить имя")
    if message.text == "Изменить контакты":
        ids = message.from_user.id
        message = bot.reply_to(message, 'Введи новые контакты')
        bot.register_next_step_handler(message, full_redact, ids, "Изменить контакты")
    if message.text == "Изменить общую информацию":
        ids = message.from_user.id
        message = bot.reply_to(message, 'Введи новую информацию')
        bot.register_next_step_handler(message, full_redact, ids, "Изменить общую информацию")
    if message.text == "Добавить товар":
        ids = str(message.from_user.id)
        user.pop(str(ids), None)
        user[str(ids)] = [str(ids)]
        message = bot.reply_to(message, 'Какого бренда вещь?')
        bot.register_next_step_handler(message, add_typec, ids)
    if message.text == "Удалить вещь":
        ids = str(message.from_user.id)
        user.pop(str(ids), None)
        message = bot.reply_to(message, 'Введи id вещи, которую хочешь удалить.\nid ты можешь найти в информации о своём профиле.')
        
        bot.register_next_step_handler(message, delc, ids)

def add_typec(message, ids):
    user[ids].append(message.text)
    bot.send_message(message.chat.id , 'Тип вещи', reply_markup=markup)
        

def delc(message, ids):
    if ids in message.text:
        user[str(ids)] = message.text
        bot.send_message(message.chat.id, telo.delete_cloth(ids, user[ids]))
    else:
        bot.send_message(message.chat.id, "Вещь не твоя, поэтому ты не можешь её удалить)")
        
def add_size(message, ids):
    if user[ids][2] in bottom:
        message = bot.send_message(message.chat.id, 'Размер вещи', reply_markup=size_niz)
    elif user[ids][2] in ["Демисезонная обувь", "Осенняя и весенняя обувь", "Зимняя обувь", "Летняя обувь", "Носки"]:
        message = bot.send_message(message.chat.id, 'Размер вещи', reply_markup=size_obv)
    else:
        message = bot.send_message(message.chat.id, 'Размер вещи', reply_markup=size_keyb)
    bot.register_next_step_handler(message, add_price, ids)

def add_price(message, ids):
    user[ids].append(message.text)
    message = bot.reply_to(message, 'Описание', reply_markup=kb)
    bot.register_next_step_handler(message, add_info, ids)

def add_info(message, ids):
    user[ids].append(message.text)
    message = bot.reply_to(message, 'Цена')
    bot.register_next_step_handler(message, add_hz, ids)

def add_hz(message, ids):
    user[ids].append(message.text)
    message = bot.reply_to(message, 'Фото')
    bot.register_next_step_handler(message, photo, 1, ids)

@bot.message_handler(content_types=['photo'])
def photo(message, flag, ids):
    user[ids].append(message.text)
    if flag == 1:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = ids + "\\" + message.photo[1].file_id + ".jpg"
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото добавлено")
        user[ids].append(src)
        print(user[ids])
        telo.add_cloth(user[ids][2], user[ids][1], user[ids][3], user[ids][5], user[ids][0], user[ids][4], user[ids][7])
        flag = 0

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup1)
    if call.data == '2':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup2)
    if call.data == '3':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup3)
    if call.data == '4':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup4)
    if call.data == '5':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup5)
    if call.data == '99':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    if call.data == 'X':
        ids = str(call.from_user.id)
        user[ids].append("Разное")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)    
    if call.data == '11':
        ids = str(call.from_user.id)
        user[ids].append("Куртка")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '12':
        ids = str(call.from_user.id)
        user[ids].append("Ветровка")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '13':
        ids = str(call.from_user.id)
        user[ids].append("Пальто")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '14':
        ids = str(call.from_user.id)
        user[ids].append("Плащ")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '15':
        ids = str(call.from_user.id)
        user[ids].append("Футболка")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '16':
        ids = str(call.from_user.id)
        user[ids].append("Майка")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '17':
        ids = str(call.from_user.id)
        user[ids].append("Свитер")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '321':
        ids = str(call.from_user.id)
        user[ids].append("Жилет")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '18':
        ids = str(call.from_user.id)
        user[ids].append("Худи")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '19':
        ids = str(call.from_user.id)
        user[ids].append("Свитшот")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '110':
        ids = str(call.from_user.id)
        user[ids].append("Компрессионное белье")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '21':
        ids = str(call.from_user.id)
        user[ids].append("Джинсы")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '22':
        ids = str(call.from_user.id)
        user[ids].append("Брюки")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '23':
        ids = str(call.from_user.id)
        user[ids].append("Шорты")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '24':
        ids = str(call.from_user.id)
        user[ids].append("Штаны")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '31':
        ids = str(call.from_user.id)
        user[ids].append("Летняя обувь")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '32':
        ids = str(call.from_user.id)
        user[ids].append("Осенняя и весенняя обувь")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '33':
        ids = str(call.from_user.id)
        user[ids].append("Зимняя обувь")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '34':
        ids = str(call.from_user.id)
        user[ids].append("Демисезоная обвувь")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '41':
        ids = str(call.from_user.id)
        user[ids].append("Портфель")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '42':
        ids = str(call.from_user.id)
        user[ids].append("Сумка")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '51':
        ids = str(call.from_user.id)
        user[ids].append("Очки")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '52':
        ids = str(call.from_user.id)
        user[ids].append("Галстук")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '53':
        ids = str(call.from_user.id)
        user[ids].append("Перчатки")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '54':
        ids = str(call.from_user.id)
        user[ids].append("Носки")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '55':
        ids = str(call.from_user.id)
        user[ids].append("Шапка")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '56':
        ids = str(call.from_user.id)
        user[ids].append("Часы")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '57':
        ids = str(call.from_user.id)
        user[ids].append("Кепка")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)
    if call.data == '58':
        ids = str(call.from_user.id)
        user[ids].append("Платок")
        message = call.message
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        add_size(message, ids)

bot.infinity_polling()

