import os
from flask import Flask
from routes import pages
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.get_default_database()
    #app.db = client.habit_tracker
    #print(client.list_database_names())

    app.register_blueprint(pages)
    return app