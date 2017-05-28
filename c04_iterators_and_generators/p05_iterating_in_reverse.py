# -*- coding:utf-8 -*-

# 问题
# 你想反方向迭代一个序列

# 解决方案
# 使用内置的 reversed() 函数，比如：
a = [1, 2, 3, 4, 5]
for x in reversed(a):
    print(x)  # 5, 4, 3, 2, 1

# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
# 如果两者都不符合，那你必须先将对象转换为一个列表才行，比如：