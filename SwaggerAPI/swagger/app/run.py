from eve import Eve
from eve_swagger import get_swagger_blueprint, add_documentation

app = Eve()
swagger = get_swagger_blueprint()
app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'My Supercool API',
    'version': '1.0',
    'description': 'an API description',
    'termsOfService': 'my terms of service',
    'schemes': ['http', 'https'],
}

# optional. Will use flask.request.host if missing.
app.config['SWAGGER_HOST'] = 'https://myhost.com'



if __name__ == '__main__':
    app.run()