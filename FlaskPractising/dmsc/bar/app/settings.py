X_DOMAINS ="*"

MONGO_URI = "mongodb://database:27017/bar"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#Domain Definition
schema = {

    'drink_type': {
        'type': 'string',
        'required': True,
        'unique': True,
    },

    'quantity': {
        'type': 'float',
        'required': True,
        'min': 0
    },

    'price': {
        'type': 'float',
        'required': True,
    }
}

bar = {

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'drink_type'
    },

    'schema': schema
}

DOMAIN = {
    'bar': bar
}