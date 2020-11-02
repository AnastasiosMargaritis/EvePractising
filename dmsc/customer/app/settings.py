X_DOMAINS ="*"

MONGO_URI = "mongodb://database:27017/customer"

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
}

DOMAIN = {
    'customer': {'schema': schema},
}