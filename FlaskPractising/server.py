from flask import Flask
from flask_restfull import Api, Resource

app = Flask(__name__)
app = Api(app)

if __name__ == '__main__':
    app.run(debug = True)