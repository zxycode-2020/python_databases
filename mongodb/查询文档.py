import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
# 连接服务器
conn = MongoClient("localhost", 27017)
# 连接数据库
db = conn.mydb
# 获取集合
collection = db.student
#查询文档
# res=collection.find({"age":{"$gt":18}})
# for item in res:
#     print(item)
#     print(type(item))
#统计查询
# res=collection.find({"age":{"$gt":18}}).count()
# print(res)

#根据ID查询
# res=collection.find({
#     "_id":ObjectId("5a1389e9a6130e80445107d2")
# })
#
# print(res[0])

#结果排序
# res=collection.find().sort("age")
#降序
# res=collection.find().sort("age",pymongo.DESCENDING)
# for row in res:
#     print(row)

#分页查询
res=collection.find().skip(3).limit(2)
for row in res:
    print(row)



#断开
conn.close()