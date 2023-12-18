#!/usr/bin/python3
"""
The file containing the Client module
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.user import Client
from flasgger.utils import swag_from


@app_views.route('/clients', methods=['GET'], strict_slashes=False)
@swag_from('documentation/client/get.yml', methods=['GET'])
def get_all_clientss():
    """ get clientss by id"""
    all_list = [obj.to_dict() for obj in storage.all(Client).values()]
    return jsonify(all_list)


@app_views.route('/çlients/<string:client_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/client/get_id.yml', methods=['GET'])
def get_client(client_id):
    """ get client by id"""
    client = storage.get(Client, client_id)
    if client is None:
        abort(404)
    return jsonify(client.to_dict())


@app_views.route('/clients/<string:client_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/client/delete.yml', methods=['DELETE'])
def del_client(client_id):
    """ delete client by id"""
    client = storage.get(Client, client_id)
    if client is None:
        abort(404)
    client.delete()
    storage.save()
    return jsonify({})


@app_views.route('/clients/', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/client/post.yml', methods=['POST'])
def create_obj_client():
    """ create new instance """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if 'email' not in request.get_json():
        return make_response(jsonify({"error": "Missing email"}), 400)
    if 'password'not in request.get_json():
        return make_response(jsonify({"error": "Missing password"}), 400)
    js = request.get_json()
    obj = Client(**js)
    obj.save()
    return (jsonify(obj.to_dict()), 201)


@app_views.route('/clients/<string:client_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/client/put.yml', methods=['PUT'])
def post_client(client_id):
    """  """
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    obj = storage.get(Client, client_id)
    if obj is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'email', 'created_at', 'updated']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict())
