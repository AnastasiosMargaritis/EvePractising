X_DOMAINS ="*"

MONGO_URI = "mongodb://localhost:27017/customer"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#Domain Definition
schema = {

    'firstname': {
        'type': 'string',
        'required': True,
        'unique': True,
    },

    'bill': {
        'type': 'float',
        'default': 0.0
    },

    'receipt': {
        'type': 'dict',
        'schema': {
            'Beer': {'type': 'float', 'default': 0.0},
            'Wine': {'type': 'float', 'default': 0.0},
            'Whiskey': {'type': 'float', 'default': 0.0},
            'Vodka': {'type': 'float', 'default': 0.0},
        }
    }
}

DOMAIN = {
    'customer': {'schema': schema},
}