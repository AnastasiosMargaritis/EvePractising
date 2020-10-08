import json
import requests

def main():
    default_data()

def url_for(endpoint):
    return "http://localhost:5000/{}".format(endpoint)

def default_data():
    data = [
        {"username": "AnasMarg", "password": "1234"},
        {"username": "KoStas", "password": "I7exw"},
        {"username": "Kwlomauros", "password": "nienie"},
        {'username': 'Sourovlakas', 'password': 'eeeerefile'}
    ]

    response = requests.post(
        url_for("user"),
        json.dumps(data),
        headers = {"Content-type": "application/json"},
    )

    print("default users posted, server response: ", response.status_code)


if __name__ == '__main__':
    main()