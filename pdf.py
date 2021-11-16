#- * -coding: utf8 - * -

from fpdf import FPDF
import os
import sqlite3
import emoji

"""pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
pdf.output("simple_demo.pdf")
"""

def show_allsal():
    text = None
    text1 = None
    try:
        sqlite_connection = sqlite3.connect("sallers.db")
        sqlite_insert_query = f"""select * from sallers;"""    
        cursor = sqlite_connection.cursor()       
        text = cursor.execute(sqlite_insert_query).fetchall()
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqqqqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    pdf = FPDF()
    pdf.add_font('DejaVu', "", 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    for i in text:
        pdf.add_page()
        pdf.multi_cell(0, 5, txt=f"id: {i[0]}", align="L")
        pdf.ln()
        pdf.multi_cell(0, 5, txt=f"Имя: {i[1]}", align="L")
        pdf.ln()
        pdf.multi_cell(0, 5, txt=f"Контакты: {i[2]}",  align="L")
        pdf.ln()
        pdf.multi_cell(0, 5, "Общая информация: " + i[3], align="L")
        pdf.ln()
    pdf.output("all_sallers.pdf")
    return "all_sallers.pdf"

def show_prof(ids):
    text = None
    text1 = None
    try:
        sqlite_connection = sqlite3.connect("sallers.db")
        sqlite_insert_query = f"""select * from sallers
                          where id = {ids};"""    
        cursor = sqlite_connection.cursor()       
        text = cursor.execute(sqlite_insert_query).fetchone()
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqqqqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

    try:
        sqlite_connection = sqlite3.connect(f"{ids}\\{ids}.db")
        sqlite_insert_query = "select * from saller;"    
        cursor = sqlite_connection.cursor()
        text1 = cursor.execute(sqlite_insert_query).fetchall()
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)
    pdf.multi_cell(0, 5, txt=f"id: {text[0]}", border="L", align="L")
    pdf.ln()
    pdf.multi_cell(0, 5, txt=f"Имя: {text[1]}", border="L", align="L")
    pdf.ln()
    pdf.multi_cell(0, 5, txt=f"Контакты: {text[2]}",  border="L", align="L")
    pdf.ln()
    pdf.multi_cell(0, 5, "Общая информация: " + text[3], border="L", align="L")
    pdf.ln()
    for i in text1:
        count = 0
        pdf.add_page()
        for j in i:
            count += 1
            if count == 1:
                pdf.multi_cell(0, 5, txt=f"id: {j}", align="L")
                pdf.ln()
            if count == 2:
                pdf.multi_cell(0, 5, txt=f"Бренд: {j}", align="L")
                pdf.ln()
            if count == 3:
                pdf.multi_cell(0, 5, txt=f"Размер: {j}", align="L")
                pdf.ln()
            if count == 4:
                pdf.multi_cell(0, 5, txt=f"Цена: {j}", align="L")
                pdf.ln()
            if count == 5:
                pdf.multi_cell(0, 5, txt=f"Описание: {j}", align="L")
                pdf.ln()
            if count == 6:
                pdf.multi_cell(0, 5, txt=f"Тип вещи: {j}", align="L")
                pdf.ln()
            if count == 7:
                pdf.image(j, x=10, y=100, w=pdf.w/2.0, h=pdf.h/2.0)



            
    pdf.output(f"{ids}.pdf")
    return f"{ids}.pdf"

