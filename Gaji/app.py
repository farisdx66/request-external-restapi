from flask import Blueprint
from flask_restful import Api
from src.resources.Gaji import GajiResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(GajiResource, '/Gaji')
