from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['SM']  # Replace with your database name

def init_db(db):
    # Initialize your database here, e.g., create collections, insert initial data
    # Example: Create a users collection if it doesn't exist
    if 'users' not in db.list_collection_names():
        db.create_collection('users')
        # Optionally, insert a sample user
        db.users.insert_one({"username": "testuser", "password": "testpass"})  # Change as needed

def get_user(db, username, password):
    # Query the database to find the user with the given username and password
    user = db.users.find_one({"username": username, "password": password})  # Adjust according to your schema
    return user