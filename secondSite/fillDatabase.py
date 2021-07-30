import os
import sqlite3

names = []

for object in os.listdir('photos'):
    if os.path.isdir('photos/{}'.format(object)):
        print(object)
        names.append(object)

name = 'chair'
conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()
sql = "Select id From catalog_furniture where idname = '{}'".format(name)
# sqlTest = """Insert into catalog_images(nameFurniture, image) values(2, 'furniture/zhurnalniy-stolik2.jpg');"""
# cur.execute(sqlTest)
# conn.commit()
cur.execute(sql)
res = cur.fetchall()
for row in res:
    print(type(row))
    print(row[0])
