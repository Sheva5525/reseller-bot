import telebot
from telebot import types
import sqlite3
import pdf
import os
from fpdf import FPDF

bot = telebot.TeleBot("2125664085:AAFBkFQn1wbwKI1-Ew9gvBzZDaaV4UTIfgk", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

user = {}
cloth = {}

accessories = ["Очки", "Галстук", "Перчатки", "Шапка", "Кепка"]

abc = ["Портфель", "Сумка", "Очки", "Галстук", "Шапка", "Часы", "Кепка", "Платок"]

size_niz = telebot.types.InlineKeyboardMarkup()
button_1 = types.InlineKeyboardButton(text="W30 L32", callback_data="W30 L32")
button_2 = types.InlineKeyboardButton(text="W32 L34", callback_data="W30 L34")
button_3 = types.InlineKeyboardButton(text="W34 L34", callback_data="W34 L34")
size_niz.row(button_1, button_2, button_3)
button_1 = types.InlineKeyboardButton(text="W36 L34", callback_data="W36 L34")
button_2 = types.InlineKeyboardButton(text="W38 L34", callback_data="W38 L34")
button_3 = types.InlineKeyboardButton(text="W40 L34", callback_data="W40 L34")
size_niz.row(button_1, button_2, button_3)
button_1 = types.InlineKeyboardButton(text="Неважно", callback_data="туз")
size_niz.add(button_1)
c = telebot.types.InlineKeyboardButton(text='размер', callback_data=6)
d = telebot.types.InlineKeyboardButton(text='тип', callback_data=61)
f = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
e = telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63)
size_niz.row(c, d, f)
size_niz.add(e)

niz_obv = ["W30 L32", "W30 L34", "W34 L34", "W36 L34", "W38 L34", "W40 L34", "37.5 (US 6.5)", "38 (US 7)", "39 (US 7.5)", "39.5 (US 8)", "40 (US 8.5)", "41 (US 9)",
           "41.5 (US 9.5)", "42 (US 10)", "43 (US 10.5)", "43.5 (US 11)", "44 (US 11.5)", "44.5 (US 12)", "45 (US 12.5)", "46 (US 13)", "47 (US 13.5)"]

size_obv = telebot.types.InlineKeyboardMarkup()
button_1 = types.InlineKeyboardButton(text="37.5 (US 6.5)", callback_data="37.5 (US 6.5)")
button_2 = types.InlineKeyboardButton(text="38 (US 7)", callback_data="38 (US 7)")
button_3 = types.InlineKeyboardButton(text="39 (US 7.5)", callback_data="39 (US 7.5)")
size_obv.row(button_1, button_2, button_3)
button_1 = types.InlineKeyboardButton(text="39.5 (US 8)", callback_data="39.5 (US 8)")
button_2 = types.InlineKeyboardButton(text="40 (US 8.5)", callback_data="40 (US 8.5)")
button_3 = types.InlineKeyboardButton(text="41 (US 9)", callback_data="41 (US 9)")
size_obv.row(button_1, button_2, button_3)
button_1 = types.InlineKeyboardButton(text="41.5 (US 9.5)", callback_data="41.5 (US 9.5)")
button_2 = types.InlineKeyboardButton(text="42 (US 10)", callback_data="42 (US 10)")
button_3 = types.InlineKeyboardButton(text="43 (US 10.5)", callback_data="43 (US 10.5)")
size_obv.row(button_1, button_2, button_3)
button_1 = types.InlineKeyboardButton(text="43.5 (US 11)", callback_data="43.5 (US 11)")
button_2 = types.InlineKeyboardButton(text="44 (US 11.5)", callback_data="44 (US 11.5)")
button_3 = types.InlineKeyboardButton(text="44.5 (US 12)", callback_data="44.5 (US 12)")
size_obv.row(button_1, button_2, button_3)
button_1 = types.InlineKeyboardButton(text="45 (US 12.5)", callback_data="45 (US 12.5)")
button_2 = types.InlineKeyboardButton(text="46 (US 13)", callback_data="46 (US 13)")
button_3 = types.InlineKeyboardButton(text="47 (US 13.5)", callback_data="47 (US 13.5)")
size_obv.row(button_1, button_2, button_3)
button_1 = types.InlineKeyboardButton(text="Неважно", callback_data="туз")
size_obv.add(button_1)
c = telebot.types.InlineKeyboardButton(text='размер', callback_data=6)
d = telebot.types.InlineKeyboardButton(text='тип', callback_data=61)
f = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
e = telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63)
size_obv.row(c, d, f)
size_obv.add(e)

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = types.KeyboardButton(text="Поиск вещи")
button_4 = types.KeyboardButton(text="Поиск продавца по id")
kb.row(button_1, button_4)

sizem = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='XXS', callback_data="XXS")
b = telebot.types.InlineKeyboardButton(text='XS', callback_data="XS")
c = telebot.types.InlineKeyboardButton(text='S', callback_data="S")
d = telebot.types.InlineKeyboardButton(text='M', callback_data="M")
e = telebot.types.InlineKeyboardButton(text='L', callback_data="L")
sizem.row(a, b)
sizem.row(c, d, e)
a = telebot.types.InlineKeyboardButton(text='XL', callback_data="XL")
b = telebot.types.InlineKeyboardButton(text='XXL', callback_data="XXL")
sizem.row(a, b)
button_1 = types.InlineKeyboardButton(text="Неважно", callback_data="туз")
sizem.add(button_1)
c = telebot.types.InlineKeyboardButton(text='размер', callback_data=6)
d = telebot.types.InlineKeyboardButton(text='тип', callback_data=61)
f = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
e = telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63)
sizem.row(c, d, f)
sizem.add(e)


markup = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Верх', callback_data=1)
b = telebot.types.InlineKeyboardButton(text='Низ', callback_data=2)
c = telebot.types.InlineKeyboardButton(text='Обувь', callback_data=3)
d = telebot.types.InlineKeyboardButton(text='Сумки', callback_data=4)
markup.row(a, b, c, d)
a = telebot.types.InlineKeyboardButton(text='Аксессуары', callback_data=5)
b = telebot.types.InlineKeyboardButton(text='Разное', callback_data="X")
markup.row(a, b)
b = telebot.types.InlineKeyboardButton(text='Неважно', callback_data="U")
markup.add(b)
a = telebot.types.InlineKeyboardButton(text='Размер', callback_data=6)
b = telebot.types.InlineKeyboardButton(text='Тип', callback_data=61)
c = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
markup.row(a, b, c)
markup.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63))

markup1 = telebot.types.InlineKeyboardMarkup()
markup1.add(telebot.types.InlineKeyboardButton(text='Куртки', callback_data=11))
a = telebot.types.InlineKeyboardButton(text='Ветровки', callback_data=12)
b = telebot.types.InlineKeyboardButton(text='Пальто', callback_data=13)
c = telebot.types.InlineKeyboardButton(text='Плащи', callback_data=14)
markup1.row(a, b, c)
a = telebot.types.InlineKeyboardButton(text='Футболки', callback_data=15)
b = telebot.types.InlineKeyboardButton(text='Майки', callback_data=16)
c = telebot.types.InlineKeyboardButton(text='Свитера', callback_data=17)
markup1.row(a, b, c)
a = telebot.types.InlineKeyboardButton(text='Худи', callback_data=18)
b = telebot.types.InlineKeyboardButton(text='Свитшот', callback_data=19)
c = telebot.types.InlineKeyboardButton(text='Компрессионное бельё', callback_data=110)
markup1.row(a, b, c)
c = telebot.types.InlineKeyboardButton(text='Жилет', callback_data=321)
markup1.add(c)
markup1.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))
a = telebot.types.InlineKeyboardButton(text='Размер', callback_data=6)
b = telebot.types.InlineKeyboardButton(text='Тип', callback_data=61)
c = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
markup1.row(a, b, c)
markup1.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63))

markup2 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Джинсы', callback_data=21)
b = telebot.types.InlineKeyboardButton(text='Брюки', callback_data=22)
c = telebot.types.InlineKeyboardButton(text='Шорты', callback_data=23)
d = telebot.types.InlineKeyboardButton(text='Штаны', callback_data=24)
markup2.row(a, b, c, d)
markup2.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))
a = telebot.types.InlineKeyboardButton(text='Размер', callback_data=6)
b = telebot.types.InlineKeyboardButton(text='Тип', callback_data=61)
c = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
markup2.row(a, b, c)
markup2.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63))

markup3 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Лето', callback_data=31)
b = telebot.types.InlineKeyboardButton(text='Осень/весна', callback_data=32)
c = telebot.types.InlineKeyboardButton(text='Зима', callback_data=33)
d = telebot.types.InlineKeyboardButton(text='Демисезон', callback_data=34)
markup3.row(a, b, c, d)
markup3.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))
a = telebot.types.InlineKeyboardButton(text='Размер', callback_data=6)
b = telebot.types.InlineKeyboardButton(text='Тип', callback_data=61)
c = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
markup3.row(a, b, c)
markup3.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63))

markup4 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Портфели', callback_data=41)
b = telebot.types.InlineKeyboardButton(text='Сумки', callback_data=42)
markup4.row(a, b)
markup4.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))
a = telebot.types.InlineKeyboardButton(text='Размер', callback_data=6)
b = telebot.types.InlineKeyboardButton(text='Тип', callback_data=61)
c = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
markup4.row(a, b, c)
markup4.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63))

markup5 = telebot.types.InlineKeyboardMarkup()
a = telebot.types.InlineKeyboardButton(text='Очки', callback_data=51)
b = telebot.types.InlineKeyboardButton(text='Галстуки', callback_data=52)
markup5.row(a, b)
a = telebot.types.InlineKeyboardButton(text='Перчатки', callback_data=53)
b = telebot.types.InlineKeyboardButton(text='Носки', callback_data=54)
markup5.row(a, b)
a = telebot.types.InlineKeyboardButton(text='Шапки', callback_data=55)
b = telebot.types.InlineKeyboardButton(text='Часы', callback_data=56)
markup5.row(a, b)
a = telebot.types.InlineKeyboardButton(text='Кепки', callback_data=57)
b = telebot.types.InlineKeyboardButton(text='Платки', callback_data=58)
markup5.row(a, b)
markup5.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data=99))
a = telebot.types.InlineKeyboardButton(text='Размер', callback_data=6)
b = telebot.types.InlineKeyboardButton(text='Тип', callback_data=61)
c = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
markup5.row(a, b, c)
markup5.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63))

def show_saller(message):
    ids = message.text
    if not os.path.exists(ids):
        return 0
    bot.send_document(message.chat.id, open(pdf.show_prof(ids), "rb"))

def is_subscribed(chat_member):
    if chat_member != 'left':
        return True
    else:
        return False

def show_me(ids):
    sqlite_connection = sqlite3.connect('sallers.db')
    cursor = sqlite_connection.cursor()
    count = list(cursor.execute(f"""SELECT * FROM sallers
                                where id = {ids}"""))
    sqlite_connection.commit()
    cursor.close()
    return count[0]

def brand_kb1(typec):
    brand_kb = telebot.types.InlineKeyboardMarkup()
    path = "cloths\\cloths.db"
    if typec == "Неважно":
        typec = ""
    try:
        sqlite_connection = sqlite3.connect(path)
        if typec != "":
            sqlite_insert_query = f"""select brend from list where typec = '{typec}';"""
        else:
            sqlite_insert_query = f"""select brend from list where typec != '{typec}';"""
        cursor = sqlite_connection.cursor()
        count = cursor.execute(sqlite_insert_query).fetchall()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlit1e2", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    count = set(count)
    lis = []
    for i in count:
        lis.append(telebot.types.InlineKeyboardButton(text=i[0], callback_data="B" + i[0]))
        if len(lis) == 3:
            brand_kb.row(lis[0], lis[1], lis[2])
            lis = []
    if len(lis) == 2:
        brand_kb.row(lis[0], lis[1])
    else:
        if len(lis) == 1:
            brand_kb.add(lis[0])
        
    button_1 = types.InlineKeyboardButton(text="Неважно", callback_data="туз2")
    brand_kb.add(button_1)   
    a = telebot.types.InlineKeyboardButton(text='Размер', callback_data=6)
    b = telebot.types.InlineKeyboardButton(text='Тип', callback_data=61)
    c = telebot.types.InlineKeyboardButton(text='Бренд', callback_data=62)
    brand_kb.row(a, b, c)
    brand_kb.add(telebot.types.InlineKeyboardButton(text='Поиск', callback_data=63))

    return brand_kb

def find_cloths(typec, size, brand):
    path = "cloths\\cloths.db"
    cloth = None
    count = 0
    a = ""
    if brand == "":
        brand = "Неважно"
    if size == "":
        size = "Неважно"
    if typec == "":
        typec = "Неважно"
    if typec != "Неважно":
        a = f"typec = '{typec}' "
    else:
        a = f"typec != '{typec}' "
    if size != "Неважно":
        a += f"and size = '{size}' "
    else:
        a += f"and size != '{size}' "
    if brand != "Неважно":
        a += f"and brend = '{brand}' "
    else:
        a += f"and brend != '{brand}' "
    try:
        sqlite_connection = sqlite3.connect(path)
        sqlite_insert_query = "select count(id) from list where " + a
        cursor = sqlite_connection.cursor()
        cloth = cursor.execute(sqlite_insert_query).fetchall()
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlit1e2", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return str(cloth[0][0])
            

@bot.message_handler(commands=['start'])
def send_welcome(message):
    ids = message.from_user.id
    if not is_subscribed(bot.get_chat_member(chat_id="@reseller_news", user_id=ids).status):
        link = f"https://t.me/reseller_news"
        bot.send_message(message.chat.id, f'Чтоб пользоваться ботом, подпишись на наш канал:\n' + link, reply_markup=kb)
        return 0
    bot.reply_to(message, "Привет, это бот для покупателей!", reply_markup=kb)


@bot.message_handler(content_types=['text'])
def main(message: types.Message):
        ids = message.from_user.id
        if not is_subscribed(bot.get_chat_member(chat_id="@reseller_news", user_id=ids).status):
            link = f"https://t.me/reseller_news"
            bot.send_message(message.chat.id, f'Чтоб пользоваться ботом, подпишись на наш канал:\n' + link)
            return 0
        if message.text == "Поиск вещи":
                ids = str(message.from_user.id)
                user[ids] = ['', '', '', '']
                user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
                r = "Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2]  + "\nНайденных вещей: " + user[ids][3] 
                bot.send_message(message.chat.id, r, reply_markup=markup)
        if message.text == "Поиск вещи по id":
                pass
        if message.text == "Поиск продавца по id":
                bot.send_document(message.chat.id, open(pdf.show_allsal(), "rb"))
                message = bot.reply_to(message, 'Введи id продавца')
                bot.register_next_step_handler(message, show_saller)

def show_cloth(brend, typec, size):
    path = "cloths\\cloths.db"
    a = ""
    if typec != "Неважно":
        a = f"typec = '{typec}' "
    else:
        a = f"typec != '{typec}' "
    if size != "Неважно":
        a += f"and size = '{size}' "
    else:
        a += f"and size != '{size}' "
    if brend != "Неважно":
        a += f"and brend = '{brend}' "
    else:
        a += f"and brend != '{size}' "
    if typec == "Разное":
        a = f"typec = '{typec}'"
    try:
        sqlite_connection = sqlite3.connect(path)
        sqlite_insert_query = "select id from list where " + a
        cursor = sqlite_connection.cursor()
        cloth = cursor.execute(sqlite_insert_query).fetchall()
        sqlite_connection.commit()
        cursor.close()
        print(cloth)
        return cloth
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlit1e2", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def send_cloth(cloths, call):
    user[str(call.from_user.id)] = []
    cloths.reverse()
    for i in cloths:
        ids = i[0].split("a")[0]
        path = ids + "\\" + ids + ".db"
        try:
            sqlite_connection = sqlite3.connect(path)
            sqlite_insert_query = f"""select * from saller where id = '{i[0]}';"""
            cursor = sqlite_connection.cursor()
            cloth = cursor.execute(sqlite_insert_query).fetchall()
            user[str(call.from_user.id)].append(cloth)
            sqlite_connection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlit1e2", error)
        finally:
            if (sqlite_connection):
                sqlite_connection.close()

def send_cloth_msg(call):
    r = ""
    ids = str(call.from_user.id)
    cloth[ids] = []
    scm = telebot.types.InlineKeyboardMarkup()
    a = telebot.types.InlineKeyboardButton(text='like', callback_data="like")
    b = telebot.types.InlineKeyboardButton(text='skip', callback_data="skip")
    scm.row(a, b)
    pdf = FPDF()
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    for i in user[ids]:
        for j in i:
            for k in j:
                cloth[ids].append(k)
        a = show_me(cloth[ids][0].split("a")[0])
        mes = "id: " + a[0] + "\nИмя: " + a[1] + "\nКонтакты: " + a[2] + "\nИнформация: " + a[3] + "\n------------------\nid: " + cloth[ids][0] + "\nТип: " + cloth[ids][5] + "\nБренд: " + cloth[ids][1] + "\nРазмер: " + cloth[ids][2] + "\nЦена: " + str(cloth[ids][3]) + "\nОписание: " + cloth[ids][4]  
        pdf.add_page()
        pdf.multi_cell(0, 5, txt=mes, align="L")
        pdf.ln()
        pdf.image(cloth[ids][6], x=10, y=140, w=pdf.w/2.0, h=pdf.h/2.0)
        #bot.send_photo(call.message.chat.id, photo = open(cloth[ids][6], 'rb'), caption = mes)
        cloth[ids] = []
        r = ""
    pdf.output("all_cloths.pdf")
    bot.send_document(call.message.chat.id, open("all_cloths.pdf", "rb"))
    

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "U":
        ids = str(call.from_user.id)
        user[ids][0] = "Неважно"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)                
    if call.data in niz_obv:
        ids = str(call.from_user.id)
        user[ids][1] = call.data
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)        
    if call.data == "туз":
        ids = str(call.from_user.id)
        user[ids][1] = "Неважно"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == "туз2":
        ids = str(call.from_user.id)
        user[ids][2] = "Неважно"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)    
    if call.data == "63":
        ids = str(call.from_user.id)
        if ((user[ids][2] != "") and (user[ids][0] != "") and (user[ids][1] == "")) or ((user[ids][2] != "") and (user[ids][0] != "") and (user[ids][1] != "")):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3], reply_markup=None)
            cloths = show_cloth(user[ids][2], user[ids][0], user[ids][1])
            send_cloth(cloths, call)
            send_cloth_msg(call)
    if call.data == '62':
        ids = str(call.from_user.id)
        brand_kb = brand_kb1(user[ids][0])
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=brand_kb)
    if call.data[0] == 'B':
        ids = str(call.from_user.id)
        user[ids][2] = call.data.split("B")[1]
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'XXS':
        ids = str(call.from_user.id)
        user[ids][1] = "XXS"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'XS':
        ids = str(call.from_user.id)
        user[ids][1] = "XS"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'S':
        ids = str(call.from_user.id)
        user[ids][1] = "S"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'M':
        ids = str(call.from_user.id)
        user[ids][1] = "M"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'L':
        ids = str(call.from_user.id)
        user[ids][1] = "L"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'XL':
        ids = str(call.from_user.id)
        user[ids][1] = "XL"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'XXL':
        ids = str(call.from_user.id)
        user[ids][1] = "XXL"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
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
    if call.data == '6':
        if user[str(call.from_user.id)][0] in ["Брюки", "Шорты", "Джинсы", "Штаны"]:
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=size_niz)
        elif user[str(call.from_user.id)][0] in ["Демисезонная обувь", "Осенняя и весенняя обувь", "Зимняя обувь", "Летняя обувь", "Носки"]:
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=size_obv)
        else: bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=sizem)
            
    if (call.data == '99') or (call.data == '61'):
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    if call.data == '11':
        ids = str(call.from_user.id)
        user[ids][0] = "Куртка"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '12':
        ids = str(call.from_user.id)
        user[ids][0] = "Ветровка"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '13':
        ids = str(call.from_user.id)
        user[ids][0] = "Пальто"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '14':
        ids = str(call.from_user.id)
        user[ids][0] = "Плащ"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == 'X':
        ids = str(call.from_user.id)
        user[ids][0] = "Разное"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '321':
        ids = str(call.from_user.id)
        user[ids][0] = "Жилет"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '15':
        ids = str(call.from_user.id)
        user[ids][0] = "Футболка"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '16':
        ids = str(call.from_user.id)
        user[ids][0] = "Майка"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '17':
        ids = str(call.from_user.id)
        user[ids][0] = "Свитер"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '18':
        ids = str(call.from_user.id)
        user[ids][0] = "Худи"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '19':
        ids = str(call.from_user.id)
        user[ids][0] = "Свитшот"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '110':
        ids = str(call.from_user.id)
        user[ids][0] = "Компрессионное белье"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '21':
        ids = str(call.from_user.id)
        user[ids][0] = "Джинсы"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '22':
        ids = str(call.from_user.id)
        user[ids][0] = "Брюки"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '23':
        ids = str(call.from_user.id)
        user[ids][0] = "Шорты"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '24':
        ids = str(call.from_user.id)
        user[ids][0] = "Штаны"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '31':
        ids = str(call.from_user.id)
        user[ids][0] = "Летняя обувь" 
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '32':
        ids = str(call.from_user.id)
        user[ids][0] = "Осенняя и весенняя обувь"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '33':
        ids = str(call.from_user.id)
        user[ids][0] = "Зимняя обувь"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '34':
        ids = str(call.from_user.id)
        user[ids][0] = "Демисезонная обувь"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '41':
        ids = str(call.from_user.id)
        user[ids][0] = "Портфель"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '42':
        ids = str(call.from_user.id)
        user[ids][0] = "Сумка"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '51':
        ids = str(call.from_user.id)
        user[ids][0] = "Очки"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '52':
        ids = str(call.from_user.id)
        user[ids][0] = "Галстук"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '53':
        ids = str(call.from_user.id)
        user[ids][0] = "Перчатки"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '54':
        ids = str(call.from_user.id)
        user[ids][0] = "Носки"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '55':
        ids = str(call.from_user.id)
        user[ids][0] = "Шапка"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '56':
        iids = str(call.from_user.id)
        user[ids][0] = "Часы"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '57':
        ids = str(call.from_user.id)
        user[ids][0] = "Кепка"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)
    if call.data == '58':
        ids = str(call.from_user.id)
        user[ids][0] = "Платок"
        user[ids][3] = find_cloths(user[ids][0], user[ids][1], user[ids][2])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тип: " + user[ids][0] + "\nРазмер: " + user[ids][1] + "\nБренд: " + user[ids][2] + "\nНайденных вещей: " + user[ids][3] , reply_markup=markup)


bot.infinity_polling()
