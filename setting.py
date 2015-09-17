#!/usr/bin/python
import json

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = 'Gear Wiki'

UPLOAD_FOLDER = './files/uploads'
UPLOAD_IMG_FOLDER = './files/img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'dmg'}
ALLOWED_IMG_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

DATA_BASE = 'sqlite:///gear_wiki.db'

FILE_TYPE = {
	'0': '-',
    '1': 'Owners Manual',
    '2': 'Service Manual',
    '3': 'Firmware',
    '4': 'Software',
    '5': 'Other',
    }

SECRET_KEY = '9EE3195AAD26ED3B76DB642552A3A'
