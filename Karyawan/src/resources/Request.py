
from flask_restful import Resource
import requests



class RequestSchema(Resource):
    def get(self):
        response = requests.get('http://127.0.0.1:5000/api/Gaji')
        return response.json()

    def post(self):
        response = requests.post('http://127.0.0.1:5000/api/Gaji')
        return response.json()

