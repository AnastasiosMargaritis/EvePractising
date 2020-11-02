
X_DOMAINS = ['http://localhost:8000',  # The domain where Swagger UI is running
             'http://editor.swagger.io',
             'http://petstore.swagger.io']

X_HEADERS = ['Content-Type', 'If-Match', 'Authorization']  # Needed for the "Try it out" buttons

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'swagger'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


description = 'Description of the schema'

schema = {

    'username': {
        'description': 'The username of the logged in user.',
        'example': 'AnasMarg',
        'type': 'string',
        'required': True
    },

    'password': {
        'description': 'The password of the logged in user,',
        'example': 'eimaiegopou1A#$',
        'type': 'string',
        'required': True
    }
}


DOMAIN = {'people': {'schema':schema},
          'math': {}}