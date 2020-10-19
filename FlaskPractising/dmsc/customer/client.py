import json
import requests

def main():
    delete_customers()
    post_customers()
    get_customers()

def url_for(endpoint):
    return "http://localhost:8082/{}".format(endpoint)


def delete_customers():
    r = requests.delete(url_for('customer'))
    print('Customers deleted, server response: ', r.status_code)
    


def post_customers():

    data = [
        {"firstname": "Anastasios", "bill": 15.99},
        {"firstname": "Kostas", "bill": 49.99},
        {"firstname": "Dimitris", "bill": 3.99},
    ]

    r = requests.post(
        url_for('customer'),
        json.dumps(data),
        headers={"Content-type": "application/json"}
    )

    print('Customers initialized, server response: ', r.status_code)

def get_customers():
    
    r = requests.get(url_for('customer'))
    print('Customers downloaded, server response: ', r.status_code)

    if r.status_code == 200:
        customers = r.json()["_items"]
        print("{} customers: ".format(len(customers)))

        for customer in customers:
            print('{}, {}'.format(customer['firstname'], customer['bill']))

if __name__ == "__main__":
    main()