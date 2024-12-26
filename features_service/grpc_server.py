import grpc
from concurrent import futures
import features_pb2
import features_pb2_grpc
from .models import UserFeatures, ItemFeatures, Interaction
from .data_transformer import DataTransformer

class FeaturesServicer(features_pb2_grpc.FeaturesServiceServicer):
    def GetUserFeatures(self, request, context):
        manager = MongoDBManager()
        collection = manager.get_collection(UserFeatures.collection_name)
        user_features = collection.find_one({'user_id': request.user_id})
        
        if not user_features:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User features not found')
            return features_pb2.UserFeaturesResponse()
            
        return features_pb2.UserFeaturesResponse(
            user_id=user_features['user_id'],
            features=user_features['features']
        )

    def GetItemFeatures(self, request, context):
        manager = MongoDBManager()
        collection = manager.get_collection(ItemFeatures.collection_name)
        item_features = collection.find_one({'item_id': request.item_id})
        
        if not item_features:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Item features not found')
            return features_pb2.ItemFeaturesResponse()
            
        return features_pb2.ItemFeaturesResponse(
            item_id=item_features['item_id'],
            features=item_features['features']
        )

    def GetInteractions(self, request, context):
        manager = MongoDBManager()
        collection = manager.get_collection(Interaction.collection_name)
        interactions = collection.find({'user_id': request.user_id})
        
        response = features_pb2.InteractionsResponse()
        for interaction in interactions:
            response.interactions.append(features_pb2.Interaction(
                user_id=interaction['user_id'],
                item_id=interaction['item_id'],
                interaction_type=interaction['interaction_type'],
                timestamp=str(interaction['timestamp'])
            ))
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    features_pb2_grpc.add_FeaturesServiceServicer_to_server(
        FeaturesServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()