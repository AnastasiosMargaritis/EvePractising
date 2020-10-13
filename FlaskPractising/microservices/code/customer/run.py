from eve import Eve
import json
import requests

app = Eve()



@app.route('/customer/order/<drink_type>/<customer_id>', methods=['POST'])
def order(drink_type, customer_id):
    bar = requests.get('http://localhost:8081/bar/order/{}'.format(drink_type))
    customer = requests.get('http://localhost:8082/customer/{}'.format(customer_id))
    print('Order downloaded, server response: ', bar.status_code)

    if bar.status_code == 200:
        r = requests.patch(
            'http://localhost:8082/customer/{}'.format(customer.json()["_id"]),
            data = {
                "firstname": str(customer.json()['firstname']),
                "bill": customer.json()['bill'] + bar.json()['price'] 
            },
            headers={"If-Match": customer.json()["_etag"]}
        )

        print('Order confired, server status: ', r.status_code)
    

    return requests.get('http://localhost:8082/customer/{}'.format(customer_id)).json()


if __name__ == '__main__':
    app.run(port=8082)