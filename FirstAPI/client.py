import json
import requests
import bcrypt
from db_testing import *

def main():
    default_data()

def url_for(endpoint):
    return "http://localhost:5000/{}".format(endpoint)

def default_data():
    salt = bcrypt.gensalt()
    data = [
        {"username": "AnasMarg", "password": bcrypt.hashpw("1234", salt)},
        {"username": "KoStas", "password": bcrypt.hashpw("I7exw", salt)},
        {"username": "Kwlomauros", "password": bcrypt.hashpw("nienie", salt)},
        {'username': 'Sourovlakas', 'password': bcrypt.hashpw('eeeerefile', salt)}
    ]

    response = requests.post(
        url_for("user"),
        json.dumps(data),
        headers = {"Content-type": "application/json"},
    )

    print("default users posted, server response: ", response.status_code)


if __name__ == '__main__':
    main()