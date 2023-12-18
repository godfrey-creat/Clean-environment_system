#!/usr/bin/python3
"""This python script ccontains Garbage_type module"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.garbage_type import Garbage_type
from flasgger.utils import swag_from


@app_views.route('/garbage_types', methods=['GET'], strict_slashes=False)
@swag_from('documentation/garbage_type/get.yml', methods=['GET'])
def get_all():
    """ Getting all by id """
    all_list = [obj.to_dict() for obj in storage.all(Garbage_type).values()]
    return jsonify(all_list)


@app_views.route('/garbage_types/<string:garbage_type_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/garbage_type/get_id.yml', methods=['GET'])
def get_method_garbage_type(garbage_type_id):
    """Get garbage_type by id."""
    garbage_type = storage.get(Garbage_type, garbage_type_id)
    if garbage_type is None:
        abort(404)
    return jsonify(garbage_type.to_dict())


@app_views.route('/garbage_types/<string:garbage_type_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/garbage_type/delete.yml', methods=['DELETE'])
def del_method(garbage_type_id):
    """ Delete garbage_type by id of garbage_type"""
    garbage_type = storage.get(Garbage_type, garbage_type_id)
    if garbage_type is None:
        abort(404)
    garbage_type.delete()
    storage.save()
    return jsonify({})


@app_views.route('/garbage_types/', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/garbage_type/post.yml', methods=['POST'])
def create_obj():
    """ create new instance """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)
    js = request.get_json()
    obj = Garbage_type(**js)
    obj.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/garbage_types/<string:garbage_type_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/garbage_type/put.yml', methods=['PUT'])
def post_method(garbage_type_id):
    """Creating  post method """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(Garbage_type, garbage_type_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
