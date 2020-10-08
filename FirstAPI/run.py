from eve import Eve
from eve.auth import BasicAuth
from db_testing import *

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return check_db(username, password)

 
if __name__ == '__main__':
    app = Eve(auth = MyBasicAuth)
    app.run()