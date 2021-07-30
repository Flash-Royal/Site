import instaloader
from instaloader import Profile, Post

instance = instaloader.Instaloader(save_metadata = False, compress_json = False)

login = "vlad.popov471@gmail.com"
password = "python1"

instance.login(user = login, passwd = password)

profile = Profile.from_username(instance.context, username = "romanov_steel_and_wood")

for highlight in instance.get_highlights(user = profile):
    for item in highlight.get_items():
        instance.download_storyitem(item, '{}'.format(highlight.title))
