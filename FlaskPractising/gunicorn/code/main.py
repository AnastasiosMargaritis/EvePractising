from flask import Flask

def create_app(testing: bool = True):
    app = Flask('__name__')

    @app.route('/')
    def index():
        return f"Hello World, my name is Anastasios<br>Testing: {testing}"
    
    @app.route('/manas')
    def manas():
        return "Gamw tin mana sou tin kargiolitsa"
        
    return app