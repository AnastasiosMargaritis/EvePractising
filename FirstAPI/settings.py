X_DOMAINS ="*"

#mongo connection string
MONGO_URI = "mongodb://localhost:27017/first-api"

#resource and item methods
RESOURCE_METHODS = ['GET']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#domain definition
people_schema = {

    'firstname': {
        'type' : 'string',
        'minlength' : 1,
        'maxlength' : 30,
        'unique'    : True
    },
    'lastname': {
        'type' : 'string',
        'minlength' : 1,
        'maxlength' : 30,
        'unique'    : True
    },
}

#domain configuration
people = {
     'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods'    : ['GET', 'DELETE'],

    'schema': people_schema
}

DOMAIN = {
    'people': people
}