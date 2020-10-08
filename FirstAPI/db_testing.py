import pymongo

def check_db(username, password):  
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["first-api"]
    mycol = mydb["user"]

    print(mycol.find_one({'username': username, 'password': password}))
    return mycol.find_one({'username': username, 'password': password})