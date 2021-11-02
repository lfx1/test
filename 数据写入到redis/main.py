import redis #调用redis库
r=redis.Redis(host='127.0.0.1',password='12345',db=1)#远程链接host=ip
pool=redis.ConnectionPool()#调用redis库里面的connectionpool链接池
r_pool=redis.Redis(connection_pool=pool)
#写入数据，查看
r.set('9','11')
print(r['9'])
print(r.get('9'))
print(type(r.get('name')))

