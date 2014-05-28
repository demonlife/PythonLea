#encoding: utf8

# http://hi.baidu.com/dooda/item/48063ef83363aace531c26bd
# http://hi.baidu.com/dooda/item/4731d151b1d919454eff20d3
import pymongo

# 建立mongo链接
mongo = pymongo.Connection(host="localhost")

# 选择数据库
db = mongo['chengmi']
# 选择表名
utbl = db['user']

'''
# 同上的用法
db = mongo.chengmi
utbl = db.user
'''

user_doc = {
    "username":"foouser",
    "emails": [
        {"email":"foouser@163.com", "primary":True},
        {"email":"foouser@gmail.com"}
    ]
}

'''
# 所有的函数都有 safe参数
# 启用安全模式插入数据，速度上会有劣势
# utbl.save(user_doc, safe=True)
r1 = utbl.insert(user_doc, safe=True)
r2 = utbl.save(user_doc, safe=True)

user_docobjid = user_doc
user_docobjid['_id'] = r1

# insert 与 save 区别：当有重复数据时，insert报错， save则会修改该数据的值为新的值
# save的功能可以记为： 有则改之，无则加之
#r1 = utbl.insert(user_docobjid, safe=True) #exception， key duplicate
r2 = utbl.save(user_docobjid, safe=True)
'''

# 删除emails中的email
#utbl.update({"username":"foouser"}, {"$pull":{"emails":{"email":"foouser@gmail.com"}}})

#utbl.save(user_doc)
# 更改某个字段中的数组中的内容需要加上 $
#utbl.update({"emails.email":"foouser@gmail.com"}, {"$set":{"emails.$.primary":True}})

# 增加子文档， 对键的值是数组的可以使用push方法，否则无法添加数据
utbl.update({"username":"foouser"},
    {"$push": {"emails":"new_email"}})

# 添加索引, 在后台添加索引，并命名索引，后两个参数不是必须的
utbl.create_index("emails.email", name="emailidx", background=True)

# 删除索引
utbl.drop_index("emailidx")
# 删除索引也可以使用创建索引的方法
utbl.create_index([("first_name", pymongo.ASCENDING), ("last_name", pymongo.ASCENDING)])
utbl.drop_index([("first_name", pymongo.ASCENDING), ("last_name", pymongo.ASCENDING)])

# 地理位置索引
utbl.create_index([("user_location", pymongo.GEO2D)], name="testgeo")

# 地理位置检索测试
utbl.find({"user_location":{"$near":[40, 40], "$maxDistance":5}}).limit(10)

# 相关区域内查找
box = [[50.73, -83.99], [50.74, -83.988]]
utbl.find({"user_location":{"$within":{"$box":box}}})
# 点（40，40）半径为5内的区域查询
utbl.find({"user_location":{"$within":{"$center":[40, 40, 5]}}}).limit(10)

# 球形区域查询
earth_radius_km = 6371.0
max_distance_km = 5.0
max_distance_radians = max_distance_km / earth_radius_km
nearest_users = utbl.find({"user_location":{"$nearSphere":[40, 40],
                                            "$maxDistance":max_distance_radians}}).limit(10)

# 插入或者更新选择， 如果有则更新，无则插入
utbl.update({"session_id":"session"}, {"$set":{"session":"description"}}, upsert=True)

# 自动增加文档属性
utbl.find_and_modify({"username":"username"}, {"$inc":{"account": 1}}, new=True)
