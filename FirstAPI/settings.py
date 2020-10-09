X_DOMAINS ="*"

#mongo connection string
MONGO_URI = "mongodb://localhost:27017/first-api"

#resource and item methods
RESOURCE_METHODS = ['GET']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#JWT Configuration
JWT_SECRET = 'secret'
JWT_ISSUER = 'issuer'

#domain definition
user_schema = {

    'username': {
        'type' : 'string',
        'minlength' : 1,
        'maxlength' : 30,
        'unique'    : True,
        'required'  : True
    },
    'password': {
        'type' : 'string',
        'minlength' : 1,
        'maxlength' : 60,
        'required'  : True
    },
    'token': {
        'type': 'string'
    }
}

#domain configuration
user = {
   
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods'    : ['GET', 'DELETE'],
    'public_methods'  : ['POST'],

    'schema': user_schema,
}

DOMAIN = {
    'user': user
}