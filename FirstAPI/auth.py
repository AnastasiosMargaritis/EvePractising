from eve.auth import TokenAuth

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        return accounts.find_one({'token': token})