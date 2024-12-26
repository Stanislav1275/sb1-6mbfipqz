from pymongo import MongoClient
from django.conf import settings

class MongoDBManager:
    def __init__(self):
        self.client = MongoClient(settings.MONGODB_URI)
        self.db = self.client[settings.MONGODB_NAME]
        
    def get_collection(self, collection_name):
        return self.db[collection_name]

class UserFeatures:
    collection_name = 'users_features'
    
    @classmethod
    def create(cls, user_id, features):
        manager = MongoDBManager()
        collection = manager.get_collection(cls.collection_name)
        return collection.insert_one({
            'user_id': user_id,
            'features': features
        })

class ItemFeatures:
    collection_name = 'items_features'
    
    @classmethod
    def create(cls, item_id, features):
        manager = MongoDBManager()
        collection = manager.get_collection(cls.collection_name)
        return collection.insert_one({
            'item_id': item_id,
            'features': features
        })

class Interaction:
    collection_name = 'interactions'
    
    @classmethod
    def create(cls, user_id, item_id, interaction_type, timestamp):
        manager = MongoDBManager()
        collection = manager.get_collection(cls.collection_name)
        return collection.insert_one({
            'user_id': user_id,
            'item_id': item_id,
            'interaction_type': interaction_type,
            'timestamp': timestamp
        })