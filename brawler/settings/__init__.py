import os

if "www/brawler_dev" in os.getcwd():
    from brawler.settings.develop import *
elif "www/brawler" in os.getcwd():
    from brawler.settings.master import *
else:
    from brawler.settings.local import *
