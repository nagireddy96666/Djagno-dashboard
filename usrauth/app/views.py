import json
from datetime import datetime
from flask import Flask, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
from usrauth.app.mongo import db
from usrauth.app.utils import serial
from usrauth.app.auth import requires_auth

app = Flask(__name__)


@requires_auth
def hello_app():
    return "Hello App"


@requires_auth
def create_user():
    if request.method == "POST":
        data = request.get_json()
        # hashed_password = generate_password_hash(data['password'], method='sha256')

        db.user.insert_one(
            {
                "userName": data['userName'],
                "password": data['password'],
                "role": data['role'],
                "firstName": data['firstName'],
                "lastName": data['lastName'],
                "email": data['email'],
                "phoneNumber": data['phoneNumber'],
                "employeeId": data['employeeId'],
                "address": data['address'],
                "pinCode": data['pinCode']
            }
        )
        context = {'message': 'User created successfully'}
        return jsonify(context)
    else:
        context = {'message': 'User creation is unsuccessful'}
        return jsonify(context)


@requires_auth
def get_users():
    if request.method == "GET":
        data = db.user.find()
        users_data = []
        for usr in data:
            serial(usr)
            user_data = {
                'id': usr["_id"],
                'name': usr['userName'],
                'role': usr['role']
            }
            users_data.append(user_data)

        """
        #  Another way of extracting data       
        users = []
        for user in data:
            serial(user)
            users.append(user)
        return jsonify(users)
        """

        return jsonify(users_data)
    else:
        context = {"message": "Users data is not available"}
        return jsonify(context)


@requires_auth
def get_one_user(key,value):
    if request.method == "GET":
        if key is 'userName' or 'email' or 'phone number':
            data = db.user.find({key: value})
            user_data = []
            for usr in data:
                serial(usr)
                user_data.append(usr)
            return jsonify(user_data)
    else:
        context = {'message': "User data does not exists with given input"}
        return jsonify(context)


@requires_auth
def get_any_user(key, value):
    import pdb; pdb.set_trace()
    if request.method == "GET":
        data = db.user.find({key:{'$exists': True}})
        user_data = []
        for usr in data:
            serial(usr)
            if usr['pinCode'] == value:
                user_data.append(usr)
        return jsonify(user_data)
    else:
        context = {'message': "User data does not exists with given input"}
        return jsonify(context)


@requires_auth
def update_user(user_id):
        user_id1 = db.user.find({"_id": user_id})
        if user_id1:
            if request.method == "PUT":
                data = request.get_json()
                db.user.update_one({"_id": ObjectId(user_id)}, {"$set": {"role": data["role"]}})
                context = {'message': 'User Updated successfully'}
                return jsonify(context)
            else:
                context = {"message": "User updation is unsuccessful"}
                return jsonify(context)
        else:
            context = {"message": "Invalid user id"}
            return jsonify(context)


@requires_auth
def delete_user(user_id):
    if request.method == "POST":
        data = request.get_json()
        user_data = db.user.delete_one({"_id": ObjectId(user_id)})
        context = {"message": "User Deleted Successfully"}
        return jsonify(context)
    else:
        context = {"message": "Invalid user, No record has been deleted"}
        return jsonify(context)