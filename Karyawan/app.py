from flask import Blueprint
from flask_restful import Api
from src.resources.Pegawai import PegawaiResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(PegawaiResource, '/Pegawai')