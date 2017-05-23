# -*- coding:utf-8 -*-

# 问题
# 你想在字节字符串上执行普通的文本操作(比如移除，搜索和替换)。

# 解决方案
# 字节字符串同样也支持大部分和文本字符串一样的内置操作。比如：

data = b'Hello World'
print(data[0:5])  # b'Hello'

print(data.startswith(b'Hello'))  # True

print(data.split())  # [b'Hello', b'World']

print(data.replace(b'Hello', b'Hello Cruel'))  # b'Hello Cruel World'

# 这些操作同样也适用于字节数组。比如：

data = bytearray(b'Hello World')
print(data[0:5])  # bytearray(b'Hello')
print(data.startswith(b'Hello'))  # True
print(data.split())  # [bytearray(b'Hello'), bytearray(b'World')]
print(data.replace(b'Hello', b'Hello Cruel'))  # bytearray(b'Hello Cruel World')