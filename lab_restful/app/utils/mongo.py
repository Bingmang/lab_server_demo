import pymongo
import gridfs
from app.config import config

print('开始连接MongoDB...')
client = pymongo.MongoClient(config.mongo_uri)
db = client[config.database]
fs = gridfs.GridFS(db)
print('成功连接MongoDB.')
