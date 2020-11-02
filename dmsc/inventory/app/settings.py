X_DOMAINS="*"

MONGO_URI = "mongodb://database:27017/inventory"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Schema Definition for Inventory Microservice.
# It consists from two fields: The drink_type and the quantity of each drink_type.
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
}

DOMAIN = {
    'inventory': {'schema': schema},
}