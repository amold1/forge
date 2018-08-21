from logger import Logger
import requests
import json

# Enable logging
log = Logger().log_to_file(__file__)


# for each in json.loads(requests.get("http://jsonplaceholder.typicode.com/posts/").content.decode('UTF-8')):
#     for key, value in each.items():
#         if key == "title" and value == "nesciunt quas odio":
#             log.info("Content: %s", each)

for each in json.loads(requests.get("http://polls.apiblueprint.org/questions").content.decode('UTF-8')):
    log.info("------------------------")
    for key, value in each.items():
        if key == "question":
            log.info("Question: %s", value)
