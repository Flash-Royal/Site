import os
from pathlib import Path
import sqlite3
from instaloader import Profile, Instaloader

class HighlightsFromInstagram():
    def __init__(self, email, password):
        self.instance = Instaloader(save_metadata = False, compress_json = False)
        self.instance.login(user = email, passwd = password)
        self.listOfNames = []

    def downloadHighlights(self, name):
        os.chdir("furniture")
        profile = Profile.from_username(self.instance.context, username = name)
        for highlight in self.instance.get_highlights(user = profile):
            self.listOfNames.append(highlight.title)
            for id, object in enumerate(highlight.get_items()):
                self.instance.download_storyitem(object, '{}'.format(highlight.title))
        os.chdir("..")


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
        if res != []:
            for row in res:
                existingNames.append(row[0])

        for name in names:
            if name not in existingNames:
                newNames.append(name)

        return newNames

    def createNewIdName(self):
        names = self.findNewNames()
        idNames = {}
        if names != []:
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

class ImageDataBase():
    def __init__(self, nameDB):
        self.conn = sqlite3.connect(nameDB)

    def findAndAddNewImages(self):
        images = []
        existingImages = []
        newImages = {}
        names = []
        cur = self.conn.cursor()
        sql = "select image from catalog_images"
        cur.execute(sql)
        res = cur.fetchall()
        if res != []:
            for row in res:
                existingImages.append(row[0])

        for object in os.listdir('furniture'):
            if os.path.isdir('furniture/{}'.format(object)):
                names.append(object)

        for name in names:
            for object in os.listdir('furniture/{}'.format(name)):
                if os.path.isfile('furniture/{}/{}'.format(name, object)):
                    if Path('furniture/{}/{}'.format(name, object)).suffix == '.jpg':
                        if object not in existingImages:
                            sql = "insert into catalog_images(nameFurniture_id, image) values((select id from catalog_furniture where name = '{0}'),'furniture/{0}/{1}')".format(name, object)
                            cur.execute(sql)
                            self.conn.commit()

inst = HighlightsFromInstagram(email = "vlad.popov471@gmail.com", password = "python1")
inst.downloadHighlights("romanov_steel_and_wood")

furniture = FurnDataBase("db.sqlite3")
furniture.addNewNames()

image = ImageDataBase("db.sqlite3")
image.findAndAddNewImages()
