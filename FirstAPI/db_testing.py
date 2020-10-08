import pymongo
import bcrypt

def check_db(username, password):  
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["first-api"]
    mycol = mydb["user"]

    print(mycol.find_one({'username': username, 'password': password}))
    return mycol.find_one({'username': username, 'password': password})

def check_db_encryption(username, password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["first-api"]
    mycol = mydb["user"]

    print(hashed)
    return mycol.find_one({'username':username, 'password': hashed})

