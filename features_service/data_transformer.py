import mysql.connector
from django.conf import settings
from .models import UserFeatures, ItemFeatures, Interaction

class MySQLConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=settings.MYSQL_DB['HOST'],
            database=settings.MYSQL_DB['NAME'],
            user=settings.MYSQL_DB['USER'],
            password=settings.MYSQL_DB['PASSWORD'],
            port=settings.MYSQL_DB['PORT']
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def close(self):
        self.cursor.close()
        self.connection.close()

class DataTransformer:
    def transform_user_features(self):
        connector = MySQLConnector()
        try:
            # Customize this query according to your MySQL schema
            connector.cursor.execute("""
                SELECT user_id, feature1, feature2, feature3
                FROM mysql_users_table
            """)
            
            for row in connector.cursor.fetchall():
                features = {
                    'feature1': row['feature1'],
                    'feature2': row['feature2'],
                    'feature3': row['feature3']
                }
                UserFeatures.create(row['user_id'], features)
        finally:
            connector.close()

    def transform_item_features(self):
        connector = MySQLConnector()
        try:
            # Customize this query according to your MySQL schema
            connector.cursor.execute("""
                SELECT item_id, feature1, feature2, feature3
                FROM mysql_items_table
            """)
            
            for row in connector.cursor.fetchall():
                features = {
                    'feature1': row['feature1'],
                    'feature2': row['feature2'],
                    'feature3': row['feature3']
                }
                ItemFeatures.create(row['item_id'], features)
        finally:
            connector.close()

    def transform_interactions(self):
        connector = MySQLConnector()
        try:
            # Customize this query according to your MySQL schema
            connector.cursor.execute("""
                SELECT user_id, item_id, interaction_type, timestamp
                FROM mysql_interactions_table
            """)
            
            for row in connector.cursor.fetchall():
                Interaction.create(
                    row['user_id'],
                    row['item_id'],
                    row['interaction_type'],
                    row['timestamp']
                )
        finally:
            connector.close()