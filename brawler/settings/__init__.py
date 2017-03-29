import os

if "project_2A_2017/brawler-services" in os.getcwd():
    from brawler.settings.master import *
# elif "www/brawler_dev" in os.getcwd():
#     from brawler.settings.develop import *
else:
    from brawler.settings.local import *
