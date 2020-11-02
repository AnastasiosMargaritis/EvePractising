import json
import requests

def main():
    delete_inventory()
    post_inventory()
    get_inventory()

def url_for(endpoint):
    return "http://localhost:8080/{}".format(endpoint)

def delete_inventory():
    r = requests.delete(url_for('inventory'))
    print('Customers deleted, server response: ', r.status_code)
    

def post_inventory():

    data = [
        {"drink_type": "Beer", "quantity": 50},
        {"drink_type": "Wine", "quantity": 50},
        {"drink_type": "Whiskey", "quantity": 50},
        {"drink_type": "Gin", "quantity": 50},
    ]

    r = requests.post(
        url_for('inventory'),
        json.dumps(data),
        headers={"Content-type": "application/json"}
    )

    print('inventory initialized, server response: ', r.status_code)

def get_inventory():
    
    r = requests.get(url_for('inventory'))
    print('inventory downloaded, server response: ', r.status_code)

    if r.status_code == 200:
        drinks = r.json()["_items"]
        print("{} drinks: ".format(len(drinks)))

        for drink in drinks:
            print('{}, {}'.format(drink['drink_type'], drink['quantity']))

if __name__ == "__main__":
    main()