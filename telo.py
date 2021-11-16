import os
import sqlite3

def get_name(typec):
    if typec.lower() in outwear:
        return 'Outwear'
    if typec.lower() in midh:
        return 'Midh'
    if typec.lower() in midl:
        return 'Midl'
    if typec.lower() in bottom:
        return 'Bottom'
    if typec.lower() in accessories:
        return 'Accessories'
    if typec.lower() in bag:
        return 'Bag'
    
def add_cloth_in_db(typec, id_cloth, brend, size):
    print(typec, id_cloth, brend, size)
    path = "cloths\\cloths.db" 
    try:
        print(typec, id_cloth, brend, size)
        sqlite_connection = sqlite3.connect(path)
        sqlite_insert_query = f"""INSERT INTO list
                          (id, typec, brend, size)
                          VALUES
                          (?, ?, ?, ?);"""    
        cursor = sqlite_connection.cursor()       
        cursor.execute(sqlite_insert_query, (id_cloth, typec, brend, size))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqliteууууууу", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    path = "BrandName\\Brand.db"
    try:
        sqlite_connection = sqlite3.connect(path)
        sqlite_insert_query = f"""select count(name) from list where name = '{brend}'"""
        print(f"""insert into list (name) values ('{brend}');""")
        cursor = sqlite_connection.cursor()
        try:
            count = cursor.execute(sqlite_insert_query).fetchone()[0]
        finally:
            sqlite_insert_query = f"""insert into list (name) values ('{brend}');"""    
            cursor = sqlite_connection.cursor()       
            cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlit1e2", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def add_saller(ids, name, contacts, inf):
    if (os.path.exists(str(ids))):
        return "Ваш профиль уже существует"
    
    os.mkdir(str(ids))
    try:
        sqlite_connection = sqlite3.connect('sallers.db')
        sqlite_insert_query = f"""INSERT INTO sallers
                          (id, name, contacts, inf)
                          VALUES
                          (?, ?, ?, ?);"""    
        cursor = sqlite_connection.cursor()
        data_tuple = (ids, name, contacts, inf)
       # cursor.execute(sql1)        
        cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

    try:
        sqlite_connection = sqlite3.connect(str(ids) + "\\" + str(ids) + '.db')

        sqlite_insert_query = f"""CREATE TABLE saller (
                              id TEXT PRIMARY KEY,
                              brend TEXT NOT NULL,
                              size TEXT,
                              price INTEGER NOT NULL,
                              inf TEXT,
                              typec TEXT,
                              photo TEXT
                              );"""    
        cursor = sqlite_connection.cursor()
        cursor.executescript(sqlite_insert_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlitwe", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def add_cloth(typec, brend, size, price, ids, inf, photo):
    #SELECT COUNT(*) FROM `table`
    try:
        sqlite_connection = sqlite3.connect(str(ids) + "\\" + str(ids) + '.db')
        cursor = sqlite_connection.cursor()
        cursor.execute("""SELECT COUNT(*) FROM saller""")
        count = cursor.fetchone()[0]
        while os.path.exists(ids + "\\" + str(ids) + "a" + str(count) + ".jpg"):
            count += 1
        id_cloth = str(ids) + "a" + str(count)
        os.rename(photo, ids + "\\" + id_cloth + ".jpg")
        photo = ids + "\\" + id_cloth + ".jpg"
        add_cloth_in_db(typec, id_cloth, brend.lower(), size)
        sqlite_insert_query = f"""INSERT INTO saller
                      (id, brend, size, price, inf, typec, photo)
                      VALUES
                      (?, ?, ?, ?, ?, ?, ?);"""    
        arg = (id_cloth, brend, size, price, inf, typec, photo)
        cursor.execute(sqlite_insert_query, arg)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlitwe", error)


def show_my_cloth(ids):
    try:
        sqlite_connection = sqlite3.connect(str(ids) + "\\" + str(ids) + '.db')
        cursor = sqlite_connection.cursor()
        count = list(cursor.execute("""SELECT * FROM saller"""))
        sqlite_connection.commit()
        cursor.close()
        print(count)
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlitwe", error)

def delete_cloth(ids, id_cloth):
    try:
        sqlite_connection = sqlite3.connect('cloths\\cloths.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"""delete FROM list where id = '{id_cloth}';""")
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlitwe", error)
    try:
        sqlite_connection = sqlite3.connect(str(ids) + "\\" + str(ids) + '.db')
        cursor = sqlite_connection.cursor()
        a = cursor.execute(f"""SELECT photo FROM saller where id = '{id_cloth}';""").fetchone()[0]
        cursor.execute(f"""delete FROM saller where id = '{id_cloth}';""")
        sqlite_connection.commit()
        cursor.close()
        os.remove(a)
        return "Вещь удалена" 
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlitwe", error)


#add_saller(ids, name, contacts, inf)

#add_cloth("Худи", "Adidas", "L", 1343, ids,"Хорошее худи. Купи или умри МАКСИМ ЧМО")

