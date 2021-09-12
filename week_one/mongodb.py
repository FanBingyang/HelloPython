import pymongo

# localhost代表本地，后面的数字代表端口
client = pymongo.MongoClient("localhost",27017)

walden = client['first'] # 创建数据库
sheet_lines = walden[''] # 创建表
