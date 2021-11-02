#列表
# 列表名=['值','值1','值2']列表的格式
list=['google','runoob','liebiao']#字符串格式
list1=[1,2,3,4,5]#数字个数
list2=['人','工','智','障']
print(list[0])#显示列表里第0个
print(list1[1])
print(list2[-1])#显示列表里倒数第一个
# 更新列表
print('第三个元素为:',list[2])
list[2]=2001
print('更新后的第三个元素为:',list[2])
list2.append('ai')
print('更新后的列表:',list2)
# 删除列表元素
print('显示原始列表:',list)
del list[2]
print('删除第三个元素:',list)
# 嵌套列表
x=[list,list1]
print(x[0])
print(x[0][1])
#元组
# 元组名=（'值'）
# 元组和列表差不多
tup=()#空元组
tup1 = ('google','runoob','liebiao')
tup2 = (1,2,3,4,5)
tup3='人','工','智','障'
#元组只有一个值时
tup4=(50)
print(type(tup4))#不加逗号为整型
tup5=(50,)
print(type(tup5))#加上逗号为元组
# 访问元组
print(tup1[0])
print(tup2[0:6])
# 删除元组
print(tup)
del tup
print('删除后的元组tup:')
# 字典
# 字典名={键:值,键1:值1,键2:值2}
d={'name':'lyy','pass':'12345','url':'www.baidu.com'}
print('d[name]:',d['name'])
print('d[pass]:',d['pass'])
# 修改字典
d['pass']='123.com'
d['url']='www.github.com'
print('d[pass]:',d['pass'])
print('d[url]:',d['url'])
# 删除字典元素
del d['name']#删除键name
# dict.clear( )#清空字典
# del  d  #删除字典
# print('d[name]:',d['name'])
#集合
#创建格式
# parame={value01,value02,……}
basket={'apple','orange','apple','paer','orange','banana'}
print(basket)#集合去重
print('orange' in basket)#快速判断元素是否在集合内
print('abc' in basket)
#两个集合之间的运算
a=set('abcadvsd')
b=set('ablfghad')
print(a-b)#集合a中包含而集合b不包含的元素
print(a|b)#集合a或b中包含所有元素
print(a&b)#集合a和b中都包含了的元素
print(a^b)#不同时包含于a和b的元素
a={x for x in 'abracadbra' if x not in 'abc'}
print(a)
#集合中添加元素
basket.add("facebook")
print(basket)
basket.update({1,2})
print(basket)
basket.update({'taobao','youku','baidu','hello,word'})
print(basket)
#移除元素
basket.remove('hello,word')
print(basket)
basket.discard('hell.word')
print(basket)#discard删除没有的元素也不会报错
basket.pop()#pop随机删除集合中的一个元素
print(basket)
#清空集合
basket.clear()
print(basket)
