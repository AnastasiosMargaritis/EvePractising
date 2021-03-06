from eve import Eve
import json
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
app.config['SWAGGER_HOST'] = 'https://customerdoc.com'  

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
    

    @app.route('/customer/order/<drink_type>/<customer_id>', methods=['POST'])
    def order(drink_type, customer_id):
        bar = requests.get('http://localhost:8081/bar/order/{}'.format(drink_type))
        customer = requests.get('http://localhost:8082/customer/{}'.format(customer_id))
        print('Order downloaded, server response: ', bar.status_code)

        if bar.status_code == 200:
            r = requests.patch(
                'http://localhost:8082/customer/{}'.format(customer.json()["_id"]),
                data = {
                    "firstname": str(customer.json()['firstname']),
                    "bill": customer.json()['bill'] + bar.json()['price'] 
                },
                headers={"If-Match": customer.json()["_etag"]}
            )

            print('Order confired, server status: ', r.status_code)
        

        return requests.get('http://localhost:8082/customer/{}'.format(customer_id)).json()
    
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

