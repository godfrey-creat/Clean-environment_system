#!/usr/bin/python3
'''Contains the bookings view for the API.'''
from flask import jsonify, request
from werkzeug.exceptions import NotFound, MethodNotAllowed, BadRequest

from api.v1.views import app_views
from models import storage, storage_t
from models.booking import Booking
from models.user import Client
from models.garbage_collection_company import Garbage_collection_company


@app_views.route('/bookings/<booking_id>/clients', methods=['GET', 'POST'])
@app_views.route('/clients/<client_id>', methods=['GET', 'DELETE', 'PUT'])
def handle_clients(client_id=None, booking_id=None):
    '''The method handler for the clients endpoint.
    '''
    handlers = {
        'GET': get_booking,
        'DELETE': remove_booking,
        'POST': add_booking,
        'PUT': update_booking,
    }
    if request.method in handlers:
        return handlers[request.method](booking_id, client_id)
    else:
        raise MethodNotAllowed(list(handlers.keys()))


def get_client(booking_id=None, client_id=None):
    '''Gets the client with the given id or all cities in
    the booking with the given id.
    '''
    if booking_id:
        booking = storage.get(Booking, booking_id)
        if booking:
            clients = list(map(lambda x: x.to_dict(), booking.clients))
            return jsonify(clients)
    elif client_id:
        client = storage.get(Client, client_id)
        if client:
            return jsonify(client.to_dict())
    raise NotFound()


def remove_client(booking_id=None, client_id=None):
    '''Removes a client with the given id.
    '''
    if client_id:
        client = storage.get(Client, client_id)
        if client:
            storage.delete(client)
            if storage_t != "db":
                for garbage_type in storage.all(Garbage_type).values():
                    if garbage_type.client_id == client_id:
                        for booking in storage.all(Booking).values():
                            if booking.garbage_type_id == garbage_type.id:
                                storage.delete(booking)
                        storage.delete(garbage_type)
            storage.save()
            return jsonify({}), 200
    raise NotFound()


def add_client(booking_id=None, client_id=None):
    '''Adds a new client.
    '''
    booking = storage.get(Booking, booking_id)
    if not booking:
        raise NotFound()
    data = request.get_json()
    if type(data) is not dict:
        raise BadRequest(description='Not a JSON')
    if 'name' not in data:
        raise BadRequest(description='Missing name')
    data['booking_id'] = booking_id
    client = Client(**data)
    client.save()
    return jsonify(client.to_dict()), 201


def update_client(booking_id=None, client_id=None):
    '''Updates the client with the given id.
    '''
    xkeys = ('id', 'booking_id', 'created_at', 'updated_at')
    if client_id:
        client = storage.get(Client, client_id)
        if client:
            data = request.get_json()
            if type(data) is not dict:
                raise BadRequest(description='Not a JSON')
            for key, value in data.items():
                if key not in xkeys:
                    setattr(client, key, value)
            client.save()
            return jsonify(client.to_dict()), 200
    raise NotFound()
