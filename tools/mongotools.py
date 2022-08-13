from config.mongoconfig import collection

#GET
# function to get the info 

def all_sentences(name):
    query = {"author":f"{name}"}
    sent = list(collection.find(query,{"_id":0}))
    return sent

#POST
# function to insert info

def inserting(dict_):
    collection.insert_one(dict_)
    return f"I inserted {dict_} into db"
   