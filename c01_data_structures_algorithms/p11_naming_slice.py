# -*- coding:utf-8 -*-

# 问题

# 你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。

# 解决方案

# 假定你有一段代码要从一个记录字符串中几个固定位置提取出特定的数据字段(比如文件或类似格式)：
# 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
# 与其那样写，为什么不想这样命名切片呢：
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# 第二种版本中，你避免了大量无法理解的硬编码下标，使得你的代码更加清晰可读了。

# 讨论
# 一般来讲，代码中如果出现大量的硬编码下标值会使得可读性和可维护性大大降低。
# 比如，如果你回过来看看一年前你写的代码，你会摸着脑袋想那时候自己到底想干嘛啊。
# 这里的解决方案是一个很简单的方法让你更加清晰的表达代码到底要做什么。

# 内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。比如：

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

# 如果你有一个切片对象a，你可以分别调用它的 a.start , a.stop , a.step 属性来获取更多的信息。比如：

a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

# 另外，你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序列上，
# 这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以满足边界限制，
# 从而使用的时候避免出现 IndexError 异常。比如：
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])

