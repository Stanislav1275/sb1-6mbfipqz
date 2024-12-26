import grpc
import features_pb2
import features_pb2_grpc

def test_service():
    # Create a channel to the server
    channel = grpc.insecure_channel('localhost:50051')
    
    # Create a stub (client)
    stub = features_pb2_grpc.FeaturesServiceStub(channel)
    
    try:
        # Test GetUserFeatures
        print("\nTesting GetUserFeatures:")
        user_request = features_pb2.UserRequest(user_id="user123")
        user_response = stub.GetUserFeatures(user_request)
        print(f"User features response: {user_response}")

        # Test GetItemFeatures
        print("\nTesting GetItemFeatures:")
        item_request = features_pb2.ItemRequest(item_id="item456")
        item_response = stub.GetItemFeatures(item_request)
        print(f"Item features response: {item_response}")

        # Test GetInteractions
        print("\nTesting GetInteractions:")
        interactions_request = features_pb2.InteractionsRequest(user_id="user123")
        interactions_response = stub.GetInteractions(interactions_request)
        print(f"Interactions response: {interactions_response}")

    except grpc.RpcError as e:
        print(f"RPC error: {e.details()}")

if __name__ == '__main__':
    test_service()