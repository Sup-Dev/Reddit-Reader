import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
scores = db.stories

def find():
    
    print("finding...")
    
    query = {'media.oembed.type':'video'}
    projection = {'media.oembed.url':1, '_id':0}
    
    try:
        cursor = scores.find(query, projection)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        
    sanity = 0
    for doc in cursor:
        print(doc)
        sanity += 1
        if (sanity > 10):
            break
            
            
find()