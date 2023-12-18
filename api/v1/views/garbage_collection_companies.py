#!/usr/bin/python3
"""
This file contains the Garbage_collection_company module.
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.garbage_collection_company import Garbage_collection_company
from flasgger.utils import swag_from


@app_views.route('/garbage_collection_companies', methods=['GET'], strict_slashes=False)
@swag_from('documentation/garbage_collection_company/get.yml', methods=['GET'])
def get_all_garbage_collection_companies():
    """ Getting garbage_collection_companies by id """
    all_list = [obj.to_dict() for obj in storage.all(Garbage_collection_company).values()]
    return jsonify(all_list)


@app_views.route('/garbage_collection_companies/<string:garbage_collection_company_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/garbage_collection_company/get_id.yml', methods=['GET'])
def get_amenity(garbage_collection_company_id):
    """ get garbage_collection_company by id"""
    garbage_collection_company = storage.get(Garbage_collection_company, garbage_collection_company_id)
    if garbage_collection_company is None:
        abort(404)
    return jsonify(garbage_collection_company.to_dict())


@app_views.route('/garbage_collection_companies/<string:garbage_collection_company_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/garbage_collection_company/delete.yml', methods=['DELETE'])
def del_garbage_collection_company(garbage_collection_company_id):
    """ delete garbage_collection_company by id"""
    garbage_collection_company = storage.get(Garbage_collection_company, garbage_collection_company_id)
    if garbage_collection_company is None:
        abort(404)
    garbage_collection_company.delete()
    storage.save()
    return jsonify({})


@app_views.route('/garbage_collection_companies/', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/garbage_collection_company/post.yml', methods=['POST'])
def create_obj_garbage_collection_company():
    """ create new instance """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    js = request.get_json()
    obj = Garbage_collection_company(**js)
    obj.save()
    return (jsonify(obj.to_dict()), 201)


@app_views.route('/garbage_collection_companies/<string:garbage_collection_company_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/garbage_collection_company/put.yml', methods=['PUT'])
def post_garbage_collection_company(garbage_collection_company_id):
    """  """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(Garbage_collection_company, garbage_collection_company_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
