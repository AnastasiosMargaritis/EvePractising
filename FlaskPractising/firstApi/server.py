from flask import Flask, jsonify, request


app = Flask(__name__)

# Initial default stores
stores = [
    {
        'name': 'PS_Store',
        'items': [
            {
                'name': 'The Exorcist',
                'price': 29.99
            }
        ]
    }
]


# POST/ store_data: {name:} creates a store 
# with no items, just the name defined
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


# GET/ store / store_name 
@app.route('/store/<string:name>')
def get_strore(name):
    # Iterates over store list
    # Returns store if the name matches
    # Else return an error message
    for store in stores:
        if store['name'] == name :
            return jsonify(store)
    return jsonify({'message': 'store not found'})


#GET/store returns all stores
@app.route('/store')
def get_all_stores():
    return jsonify({'stores': stores})


# POST / store_name / item returns the items of a store
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})


# GET / store_name / item returns the items of a store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})


# main
if __name__ == '__main__':
    app.run()