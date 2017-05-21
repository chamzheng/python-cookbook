# -*- coding:utf-8 -*-

# 问题
# 现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？
#
# 解决方案
# 任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。
# 唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
p = (4, 5)
x, y = p
print(x)
print(y)

print('---------------------')
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)
name, shares, price, (year, month, day) = data
print(name)
print(shares)
print(price)
print(year)
print(month)
print(day)
# 讨论
# 实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器。

s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)

# 有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况Python并没有提供特殊的语法。
# 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
# 你必须保证你选用的那些占位变量名在其他地方没被使用到。
