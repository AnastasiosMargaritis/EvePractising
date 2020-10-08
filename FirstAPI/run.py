from eve import Eve
from eve.auth import BasicAuth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == 'admin' and password == 'secret'


app = Eve(auth = MyBasicAuth)

if __name__ == '__main__':
    app.run()