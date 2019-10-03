
from flask_restful import Resource
import requests
import json
from urllib.request import urlopen


class RequestSchema(Resource):
    def get(self):
        # url = format(url_base)
        url_base = urlopen('http://127.0.0.1:5000/api/Gaji').read()
        response = requests.get(url_base).text

        if response.status_code == 200:
            return json.load(response.decode('utf-8'))
        else:
            return None



        # print(url_base)

