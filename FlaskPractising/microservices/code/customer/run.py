from eve import Eve
import json
import requests

app = Eve()

@app.route('/order')
def order():
    return 's'

if __name__ == '__main__':
    app.run(port=8082)