from models import UserFeatures, ItemFeatures, Interaction
from datetime import datetime

def seed_test_data():
    # Seed user features
    user_features = {
        'feature1': 'value1',
        'feature2': 'value2',
        'feature3': 'value3'
    }
    UserFeatures.create('user123', user_features)
    print("Created test user features")

    # Seed item features
    item_features = {
        'feature1': 'itemval1',
        'feature2': 'itemval2',
        'feature3': 'itemval3'
    }
    ItemFeatures.create('item456', item_features)
    print("Created test item features")

    # Seed interactions
    Interaction.create(
        'user123',
        'item456',
        'click',
        datetime.now()
    )
    print("Created test interaction")

if __name__ == '__main__':
    seed_test_data()