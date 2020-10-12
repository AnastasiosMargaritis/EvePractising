X_DOMAINS ="*"

MONGO_URI = "mongodb://localhost:27017/inventory"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# #Domain Definition
schema = {

    'drink_type': {
        'type': 'string',
        'required': True,
        'unique': True,
    },

    'quantity': {
        'type': 'float',
        'required': True,
    },
}

DOMAIN = {
    'inventory': {'schema': schema},
}