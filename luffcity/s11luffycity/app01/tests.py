from django.test import TestCase
import redis


conn = redis.Redis(host='192.168.37.131', port=6379)
# 设置值
conn.set('name', '洪俊')
# 获取值
val = conn.get('name').decode('utf8')
print(val)

# conn = redis.Redis(host='192.168.11.61', port=6379)
# # 设置值
# # conn.set('hongjun_name', '洪俊')
# # 获取值
# # conn.delete('hongjun_name')
# val = conn.get('hongjun_name').decode('utf8')
# print(val)
