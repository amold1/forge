from logger import Logger
from requests import request
import json

# Enable logging
log = Logger().log_to_file(__file__)

def jsonplaceholder():
    for each in json.loads(requests.get("http://jsonplaceholder.typicode.com/posts/").content.decode('UTF-8')):
        log.info(each)
        if each["userId"] == 1 and each["id"] == 1:
            log.info(each["title"])
        for key, value in each.items():
            if key == "title" and value == "nesciunt quas odio":
                log.info("Content: %s", each)
