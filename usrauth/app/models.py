import datetime
from usrauth.app.mongo import db

user = {'userName': 'naveen',
        'password': 'Developer',
        'role': '',
        'firstName': '',
        'lastName': '',
        'email': '',
        'phoneNumber': '',
        'employeeId': '',
        'address': '',
        'pinCode': '',
        'createdDate': datetime.datetime.utcnow()
        }

result = db.users.insert_one(user)