from requests import request
import json

class APIARY():
    def __init__(self):

        self.URL = "http://polls.apiblueprint.org/questions"
        self.HEADERS = {"Content-Type": "application/json"}

    def _make_request(self, method="GET", data=None):

        if method in ["GET", "DELETE"]:
            return json.loads(request(url=self.URL, method=method, headers=self.HEADERS).content.decode('UTF-8'))
        else:
            return request(url="{}".format(self.URL), method=method, data=json.dumps(data), headers=self.HEADERS).status_code

    def post_question(self, question, choices):

        data = {"question": question, "choices": choices}
        new_question = self._make_request(data=data, method="POST")
        log.info(new_question)
        return self._make_request()
