
import pymongo
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    # loads environment variables from .env file for local environment, production env variables are setup separately
    load_dotenv()

    client_url = f'mongodb+srv://{os.getenv("MONGODB_USERNAME")}:{os.getenv("MONGODB_PASSWORD")}'\
                 f'{os.getenv("MONGODB_CLUSTER_DATABASE_URL")}'
    client = pymongo.MongoClient(client_url)
    print(client_url)
    db = client.test
