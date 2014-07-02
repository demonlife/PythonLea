#encoding:utf8

#list中的字典排序, 使用多个字段排序
person = [{'name':'aab', 'age':10, 'cnt':100},
          {'name':'aab', 'age':22, 'cnt':89},
          {'name':'aab', 'age':22, 'cnt':98},
          {'name':'abc', 'age':11, 'cnt':68},
          {'name':'aab', 'age':25, 'cnt':20}]
# 按姓名的升序排序，如果姓名相同则按年龄的降序排列， 然后按cnt升序排列
d = sorted(person, key=lambda x:(x['name'], -x['age'], x['cnt']))
print d

# 单独对字典排序
from operator import itemgetter
phonebook = {'Linda':'7750', 'Bob': '9345', 'Carol':'5834'}

sorted_pb = sorted(phonebook.iteritems(), key=itemgetter(1))

# 多维list排序
gameresult = [['Bob', 95, 'A'],['Alan', 86, 'C'], ['Mandy', 82.5, 'A']]
sorted(gameresult, key=itemgetter(2, 1))

# 字典中混合list排序

mydict = {'Li':['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3]
      }
sorted(mydict.iteritems(), key=lambda (k,v): itemgetter(1)(v))

