from flask import request
from flask_restful import Resource
from src.models.Model import db, Gaji, GajiSchema

gajis_schema = GajiSchema(many=True)
gaji_schema = GajiSchema()

class GajiResource(Resource):
    def get(self):
        gajis = Gaji.query.all()
        gajis = gajis_schema.dump(gajis).data
        return {'status': 'success', 'data': gajis}, 200
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        data, errors = gaji_schema.load(json_data)
        if errors:
            return errors, 422
        gaji = Gaji.query.filter_by(name=data['name']).first()
        if gaji:
            return {'message': 'name already exists'}, 400
        gaji = Gaji(
            name=json_data['name'],
            gaji=json_data['gaji']
        )

        db.session.add(gaji)
        db.session.commit()

        result = gajis_schema.dump(gaji).data

        return {"status": 'success', 'data': result}, 201