from eve import Eve
from eve.auth import BasicAuth, TokenAuth
import bcrypt
from db_testing import *

#BCrypt Authentication 
class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['user']
        account = accounts.find_one({'username': username})
        return account and bcrypt.hashpw(password, account['password']) == account['password']


#Token Based Authentication
class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        accounts = app.data.driver.db['user']
        return accounts.find_one({'token': token})

if __name__ == '__main__':
    app = Eve(auth = TokenAuth)
    app.run()