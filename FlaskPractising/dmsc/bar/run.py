from eve import Eve
import requests

def create_app():
    app = Eve()

    @app.route('/bar/order/<drink_type>', methods=['GET'])
    def bar_order(drink_type):
        r = requests.get('http://localhost:8081/bar/{}'.format(drink_type))
        print('Drink located, server status: ', r.status_code)

        if r.status_code == 200:
            r = requests.patch(
                'http://localhost:8081/bar/{}'.format(r.json()["_id"]), 
                data = {
                    "drink_type": str(r.json()['drink_type']),
                    "quantity": r.json()['quantity'] - 1,
                    "price": r.json()['price']
                    },
                headers={"If-Match": r.json()["_etag"]}
                )
            print('Quantity updated, server status: ', r.status_code)
        
        return requests.get('http://localhost:8081/bar/{}'.format(drink_type)).json()

    return app