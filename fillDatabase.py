import os
import sqlite3

class FurnDataBase():
    def __init__(self, nameDB):
        self.conn = sqlite3.connect(nameDB)

    def findNewNames(self):
        newNames = []
        names = []
        existingNames = []

        for object in os.listdir('furniture'):
            if os.path.isdir('furniture/{}'.format(object)):
                names.append(object)

        cur = self.conn.cursor()
        sql = "select name from catalog_furniture"
        cur.execute(sql)

        res = cur.fetchall()
        for row in res:
            if row[0] != '':
                existingNames.append(row[0])

        for name in names:
            if name not in existingNames:
                newNames.append(name)

        return newNames

    def createNewIdName(self):
        names = self.findNewNames()
        idNames = {}

        print("Enter idNames for new names")
        for name in names:
            idNames[name] = str(input("{}: ".format(name)))

        return names, idNames

    def addNewNames(self):
        names, idNames = self.createNewIdName()
        image = {}
        cur = self.conn.cursor()
        for name in names:
            for object in os.listdir('furniture/{}'.format(name)):
                if os.path.isfile('furniture/{}/{}'.format(name, object)):
                    image[name] = 'furniture/{}/{}'.format(name, object)
                    break
            sql = "insert into catalog_furniture(idName,name,imageBack) values('{}', '{}', '{}')".format(idNames[name], name, image[name])
            cur.execute(sql)
            self.conn.commit()

furniture = FurnDataBase("db.sqlite3")
furniture.addNewNames()

# names = []
# images = {}
# for object in os.listdir('furniture'):
#     if os.path.isdir('furniture/{}'.format(object)):
#         names.append(object)
#
# print(names)
#
# for name in names:
#     files = []
#     for object in os.listdir('furniture/{}'.format(name)):
#         if os.path.isfile('furniture/{}/{}'.format(name, object)):
#             files.append(object)
#     images[name] = files
#
# print(images)
# conn = sqlite3.connect("db.sqlite3")
# cur = conn.cursor()
# sql = "Select id, name, idName, imageBack From catalog_furniture where idname = '{}'".format(name)
# sql1 = "Select nameFurniture_id from catalog_images"
# cur.execute(sql1)
# res = cur.fetchall()
# print(res[0])

# sqlTest = "Insert into catalog_images(nameFurniture_id, image) values((Select id From catalog_furniture where idname = '{}'), 'furniture/Стулья/2020-10-04_19-52-20_UTC.jpg');".format(name)
# cur.execute(sqlTest)
# conn.commit()
