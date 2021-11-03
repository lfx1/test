import pika

#建立连接
userx=pika.PlainCredentials("admin","123.com")
conn=pika.BlockingConnection(pika.ConnectionParameters("192.168.1.10",5672,'/',credentials=userx))

#开辟管道
channelx=conn.channel()

#声明队列，参数为队列名
channelx.queue_declare(queue="abc")

#发送数据，发送一条，如果要发送多条则复制此段
channelx.basic_publish(exchange="",
                       routing_key="abc",# 队列名
                       body="abc" # 发送的数据
                       )
print("--------发送数据完成-----------")

#关闭连接
conn.close()
# ----
# ----


#消息处理函数，执行完成才说明接收完成，此时才可以接收下一条，串行
def dongcallbackfun(v1,v2,v3,bodyx):
    print("得到的数据为:",bodyx)

#接收准备
channelx.basic_consume(dongcallbackfun, #收到消息的回调函数
                       queue="dongchannel11", #队列名
                       no_ack=True #是否发送消息确认
                       )
print("-------- 开始接收数据 -----------")

#开始接收消息
channelx.start_consuming()