from eve import Eve
from eve.auth import BasicAuth
import bcrypt
from db_testing import *

class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['user']
        account = accounts.find_one({'username': username})
        return account and bcrypt.hashpw(password, account['password']) == account['password']


if __name__ == '__main__':
    app = Eve(auth = BCryptAuth)
    app.run()