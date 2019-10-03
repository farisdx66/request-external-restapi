from flask import Blueprint
from flask_restful import Api
from src.resources.Pegawai import PegawaiResource
from src.resources.Request import RequestSchema

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(PegawaiResource, '/Pegawai')
api.add_resource(RequestSchema, '/Request')