from eve import Eve
import requests
import logging
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
app.config['SWAGGER_HOST'] = 'https://bardoc.com'  

def log_every_get_request(resource, request, payload):
    app.logger.info(request)

def log_every_post(resource, request):
    app.logger.info(resource)

def log_every_delete(resource, request, payload):
    app.logger.info(payload)

@app.after_request
def after(response):
    app.logger.info(response)
    return response

app.on_post_GET += log_every_get_request
app.on_pre_POST += log_every_post
app.on_pre_DELETE += log_every_delete

def create_app():


    @app.route('/bar/order/<drink_type>', methods=['GET'])
    def bar_order(drink_type):
        r = requests.get('http://localhost:8081/bar/{}'.format(drink_type))
        print('Drink located, server status: ', r.status_code)

        if r.status_code == 200:
            r = requests.patch(
                'http://localhost:8081/bar/{}'.format(r.json()["_id"]), 
                data = {
                    "drink_type": str(r.json()['drink_type']),
                    "quantity": r.json()['quantity'] - 1,
                    "price": r.json()['price']
                    },
                headers={"If-Match": r.json()["_etag"]}
                )
            print('Quantity updated, server status: ', r.status_code)
        
        return requests.get('http://localhost:8081/bar/{}'.format(drink_type)).json()

    # enable logging to 'app.log' file
    handler = logging.FileHandler('app.log')

    # set a custom log format, and add request
    # metadata to each log line
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d] -- ip: %(clientip)s, '
        'url: %(url)s, method:%(method)s'))

    # the default log level is set to WARNING, so
    # we have to explictly set the logging level
    # to INFO to get our custom message logged.
    app.logger.setLevel(logging.INFO)

    # append the handler to the default application logger
    app.logger.addHandler(handler)

    return app