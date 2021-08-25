from instaloader import Profile, Instaloader
import os


class HighlightsFromInstagram():
    def __init__(self, email, password):
        self.instance = Instaloader(save_metadata = False, compress_json = False)
        self.instance.login(user = email, passwd = password)
        self.listOfNames = []

    def downloadHighlights(self, name):
        os.chdir("test")
        profile = Profile.from_username(self.instance.context, username = name)
        for highlight in self.instance.get_highlights(user = profile):
            self.listOfNames.append(highlight.title)
            for id, object in enumerate(highlight.get_items()):
                self.instance.download_storyitem(object, '{}'.format(highlight.title))

inst = HighlightsFromInstagram(email = "vlad.popov471@gmail.com", password = "python1")
inst.downloadHighlights("romanov_steel_and_wood")
