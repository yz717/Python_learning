# 列表的定义
# 名字[]
name_list = ['717','yz']
print(name_list)
print(type(name_list))
# 可以为不同类型
# 也可以嵌套(即列表嵌列表)

# 列表的下标索引
print(name_list[0])
print(name_list[1])
# 反向列表索引 即从后往前-1，-2，-3 ...
print(name_list[-1])
print(name_list[-2])
# 嵌套列表
list = [[1,2,3],[4,5,6],7,8,9]
print(list[2])


# 函数定义在类成员中称为方法
# 列表的常用操作


# 查找元素的下标
my_list = [1,2,3,4,5,6,7,8,9]
index = my_list.index(1)
print(index)

# 修改特定位置的值
# 列表[下标] = 值
my_list[2] = 10
print(my_list)

# 列表中元素的插入
# 列表.insert(下标，元素)
list = ['abc','def','ghi','jkl','mno']
list.insert(0,'qwer')
print(list)
my_list.insert(0,10)
print(my_list)

# 追加即在尾部插入一个元素
# 列表.append(元素)
my_list.append(10)
print(my_list)

# 追加一批元素
# 列表.extend(其他数据容器)
my_list.extend([-1,-2,-3,-4])
print(my_list)


# 元素删除
# 语法1  del列表[下标]
del my_list[0]
print(my_list)
# 语法2  列表.pop(下标)
# 可用变量接受删除的值
ele = my_list.pop(0)
print(my_list)
print(ele)


# 删除某元素在列表的  第一个  匹配项
# 列表.remove(元素)
list = ['abc','def','abc','ghi','abc','jkl','mno']
list.remove('abc')
print(list)


# 清空列表
# 列表.clear()
list.clear()
print(list)


# 统计某元素在列表中的数量
# 列表.count(元素)
print(my_list.count(4))


# 列表的元素数量
# len(列表)
count = len(my_list)
print(my_list)
print(count)

list =[21,25,21,23,22,20]
print(list)
list.append(31)
print(list)
list.extend([29,33,30])
print(list)
num_first = list[0]
print(num_first)
num_last = list[-1]
print(num_last)
index = list.index(31)
print(index)
print(list)