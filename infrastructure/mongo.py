from dotenv import load_dotenv
from pymongo import MongoClient
from os import getenv, getcwd, path

load_dotenv(override=True)

USERNAME = getenv("username")
PASSWORD = getenv("password")
HOST = getenv("host")
PORT = getenv("port")
DATABASE = getenv("port")
PROTOCOL = getenv("protocol")

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
cert_path = path.join(getcwd(),"ca-certificate.crt")
engine_string = f"{PROTOCOL}://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?authSource=admin&replicaSet=mongo-db-crud&tls=true&tlsCAFile={cert_path}"
client = MongoClient(engine_string)

db = client.admin
