import json
import requests

def main():
    post_bar()
    get_bar()

def url_for(endpoint):
    if endpoint == "inventory":
        return "http://localhost:8080/{}".format(endpoint)
    return "http://localhost:8081/{}".format(endpoint)

def post_bar():
    r = requests.get(url_for("inventory"))
    print('Inventory initialized, server response: ', r.status_code)

    if r.status_code == 200:
        drinks = r.json()["_items"]
        new_drinks = []

        for drink in drinks:
            if drink["drink_type"] == "Beer":
                drink["price"] = 3.99
                print('Beer')
            elif drink['drink_type'] == 'Wine':
                drink['price'] = 4.99
            elif drink['drink_type'] == 'Whiskey':
                drink['price'] = 6.99
            else:
                drink['price'] = 7.99
            
            new_drinks.append({"drink_type": str(drink['drink_type']), "quantity": drink['quantity'], "price": drink['price']})

    print(new_drinks)
    r = requests.post(
        url_for("bar"),
        json.dumps(new_drinks),
        headers={"Content-type": "application/json"}
    )

    print('Bar filled from inventory, server response: ', r.status_code)

def get_bar():
    r = requests.get(url_for('bar'))
    print('inventory downloaded, server response: ', r.status_code)

    if r.status_code == 200:
        drinks = r.json()["_items"]
        print("{} drinks: ".format(len(drinks)))

        for drink in drinks:
            print('{}, {}'.format(drink['drink_type'], drink['price']))

if __name__ == "__main__":
    main()