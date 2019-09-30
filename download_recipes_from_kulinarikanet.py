import requests
import logging
import os
import time

start = 1
end = 22040
folder = "data"

logging.basicConfig(filename="kulinarika.net.log", level=logging.INFO)

recipe_link = "https://www.kulinarika.net/recepti/"
error_link = "https://www.kulinarika.net/napaka/?error=1"

for i in range(start, end):
    time.sleep(1)
    data = requests.get(recipe_link + str(i))
    if data.status_code == 200 and data.url != error_link:
        filename = "-".join(data.url.strip().split("/")[-4:-1]) + ".html"
        with open(os.path.join("data", filename), "w") as f:
            f.write(data.text)
    elif data.url == error_link:
        logging.info(str(i) + ": Error page")
    else:
        logging.info(str(i) + ": " + str(data.status_code))
