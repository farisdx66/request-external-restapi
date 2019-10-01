from flask import request
from flask_restful import Resource
from src.models.Model import db, Pegawai, PegawaiSchema

pegawais_schema = PegawaiSchema(many=True)
pegawai_schema = PegawaiSchema()

class PegawaiResource(Resource):
    def get(self):
        pegawais = Pegawai.query.all()
        pegawais = pegawais_schema.dump(pegawais).data
        return {'status': 'success', 'data': pegawais}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = pegawai_schema.load(json_data)
        if errors:
            return errors, 422
        pegawai = Pegawai.query.filter_by(name=data['name']).first()
        if pegawai:
            return {'message': 'pegawai already exists'}, 400
        pegawai = Pegawai(
            name=json_data['name'],
            alamat=json_data['alamat']
        )

        db.session.add(pegawai)
        db.session.commit()

        result = pegawai_schema.dump(pegawai).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = pegawai_schema.load(json_data)
        if errors:
            return errors, 422
        pegawai = Pegawai.query.filter_by(id=data['id']).first()
        if not pegawai:
            return {'message': 'Category does not exist'}, 400
        pegawai.name = data['name']
        pegawai.alamat = data['alamat']
        db.session.commit()

        result = pegawai_schema.dump(pegawai).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = pegawai_schema.load(json_data)
        if errors:
            return errors, 422
        pegawai = Pegawai.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = pegawai_schema.dump(pegawai).data

        return {"status": 'success', 'data': result}, 204