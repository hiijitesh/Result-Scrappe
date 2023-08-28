from pymongo import MongoClient
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

mongo_url = os.environ.get("MONGO_URL")
if not mongo_url:
    raise Exception("MONGO_URL environment variable not set")

client = MongoClient(mongo_url)
db = client["BOT"]
collection = db["Results"]


def insert_result(result_data):
    result_data.pop("_id", None)
    collection.insert_one(result_data)


def find_update_existing_result(RegistrationNo, Student):
    """it will update the existing result in database

    Args:
        RegistrationNo (number): reg num which help to find existing data
        Student (dict): student result data
    """
    # count = collection.find_one({"Registration No": RegistrationNo})
    # if count:
    collection.find_one_and_update(
        {"Registration No": RegistrationNo}, {"$set": Student}, upsert=True
    )
    print("result found:", RegistrationNo)
    logger.info(f"result updated:{RegistrationNo}")
    # else:
    #     insert_result(Student)
    #     logger.info("new result inserted: ", RegistrationNo)
    #     print("new result inserted into database: ", RegistrationNo)
