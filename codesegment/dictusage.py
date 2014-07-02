#encoding:utf8

#字典排序, 使用多个字段排序
person = [{'name':'aab', 'age':10, 'cnt':100},
          {'name':'aab', 'age':22, 'cnt':89},
          {'name':'aab', 'age':22, 'cnt':98},
          {'name':'abc', 'age':11, 'cnt':68},
          {'name':'aab', 'age':25, 'cnt':20}]
# 按姓名的升序排序，如果姓名相同则按年龄的降序排列， 然后按cnt升序排列
d = sorted(person, key=lambda x:(x['name'], -x['age'], x['cnt']))
print d

