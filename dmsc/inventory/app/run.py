from eve import Eve
import logging

app = Eve()

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

