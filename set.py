# 集合
# 变量名 = {}
# 空集合 a = set()
set1 = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,78}
print(set1)
print(type(set1))
# 去重 无序

# 添加
# set.add()
set1.add("Hello")
print(set1)

# 移除
# set.remove()
set1.remove("Hello")
print(set1)

# 随机取出一个元素
# set.pop()
result = set1.pop()
print(result)
print(set1)

# 清空集合
# set.clear()
set1.clear()
print(set1)

# 取出两个集合的差集
# 语法 ：集合1.difference(集合2)
# 功能 ：取出集合1和集合2的差集(集合1有而集合2没有的)
# 结果 ：得到一个新集合
set1 = {1,2,3,4,5,6}
set2 = {1,2,3,7,8,9}
new_set = set1.difference(set2)
print(new_set)

# 消除两个集合的差集
# 语法 ：集合1.difference_updata(集合2)
# 功能 ：对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果 ：集合1被修改，集合2不变
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
new_set = set1.difference(set2)
print(new_set)

# 合并两个集合
# 语法 ： 集合1.union(集合2)
# 功能 ：合并
# 结果 ：得到新集合
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
new_set = set1.union(set2)
print(new_set)

# 统计集合内元素数量
# len()

# 遍历
# 不支持下标索引  故不能用while
set1 = {1,2,3,4,5,6}
for i in set1:
    print(i)

myliist = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itcast','best']
set = set()
for i in myliist:
    set.add(i)
print(set)