import mysql.connector

cnx = mysql.connector.connect(user="root", password="root", host="127.0.0.1", database="NOA_LTC_CHANGE_ORDERS")


add_change_order = ("INSERT INTO NOA_LTC_CHANGE_ORDERS "
                    "(TAX_YEAR, BATCH_NO) "
                    "VALUES (2025, 1)")

cursor = cnx.cursor()

cursor.execute(add_change_order)

cnx.commit()
cursor.close()
cnx.close()