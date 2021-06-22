import http.client
import urllib
import json
from main import *


conn = http.client.HTTPConnection(host='eu.api.3dbinpacking.com', port=80)

data = {
    "bins": [{"w": container.getBreedteC(), "h": container.getHoogteC(), "d": container.getLengteC(), "max_wg": 0, "id": "Container"}],

    "items": [{"w": fitnessBankje.getBreedte(), "h": fitnessBankje.getHoogte(), "d": fitnessBankje.getLengte(), "q": fitnessbankjeQ, "vr": 1, "wg": 0, "id": "Fitnessbankje"},

              {"w": fitnessMat1.getBreedte(), "h": fitnessMat1.getHoogte(), "d": fitnessMat1.getLengte(), "q": fitnessmatQ, "vr": 1, "wg": 0, "id": "FitnessMat"},

              {"w": flessen.getBreedte(), "h": flessen.getHoogte(), "d": flessen.getLengte(), "q": flessenQ, "vr": 1, "wg": 0, "id": "Flessen"},

              {"w": voetballen.getBreedte(), "h": voetballen.getHoogte(), "d": voetballen.getLengte(), "q": voetballenQ, "vr": 1, "wg": 0, "id": "Voetballen"}],

    "username": "martin.rog",
    "api_key": "5633da16b9f7c6337cc4be333ab05cff",
    "params": {"images_background_color": "192,192,192", "images_bin_border_color": "59,59,59",
               "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79",
               "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103",
               "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133",
               "images_width": 250, "images_height": 250, "images_source": "file", "images_sbs": 1,"images_complete": 1}}

params = urllib.parse.urlencode(({'query': json.dumps(data)}))
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn.request("POST", "/packer/pack", params, headers)
content = conn.getresponse().read()
conn.close()



print("VISUALISATION DATA:\n\n",
      content)
quit()
