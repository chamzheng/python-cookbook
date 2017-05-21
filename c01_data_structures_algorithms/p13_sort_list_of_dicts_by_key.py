# -*- coding:utf-8 -*-

# 问题
# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

# 解决方案
# 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。
# 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：
from operator import itemgetter

rows = [
    {'first_name': 'Brian', 'last_name': 'Jones', 'uid': 1003},
    {'first_name': 'David', 'last_name': 'Beazley', 'uid': 1002},
    {'first_name': 'John', 'last_name': 'Cleese', 'uid': 1001},
    {'first_name': 'Big', 'last_name': 'Jones', 'uid': 1004}
]

# 根据任意的字典字段来排序输入结果行是很容易实现的，代码示例：
rows_by_first_name = sorted(rows, key=itemgetter('first_name'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_first_name)
print(rows_by_uid)

# itemgetter() 函数也支持多个keys，比如下面的代码
rows_by_lfname = sorted(rows, key=itemgetter('last_name', 'first_name'))
print(rows_by_lfname)

# 讨论
# 在上面例子中， rows 被传递给接受一个关键字参数的 sorted() 内置函数。
# 这个参数是 callable 类型，并且从 rows 中接受一个单一元素，然后返回被用来排序的值。
# itemgetter() 函数就是负责创建这个 callable 对象的。

# operator.itemgetter() 函数有一个被 rows 中的记录用来查找值的索引参数。
# 可以是一个字典键名称， 一个整形值或者任何能够传入一个对象的 __getitem__() 方法的值。
# 如果你传入多个索引参数给 itemgetter() ，它生成的 callable 对象会返回一个包含所有元素值的元组，
# 并且 sorted() 函数会根据这个元组中元素顺序去排序。
# 但你想要同时在几个字段上面进行排序(比如通过姓和名来排序，也就是例子中的那样)的时候这种方法是很有用的。

# itemgetter() 有时候也可以用 lambda 表达式代替，比如：
rows_by_first_name = sorted(rows, key=lambda r: r['first_name'])
rows_by_lfname = sorted(rows, key=lambda r: (r['last_name'], r['first_name']))

# 这种方案也不错。但是，使用 itemgetter() 方式会运行的稍微快点。因此，如果你对性能要求比较高的话就使用 itemgetter() 方式。
# 最后，不要忘了这节中展示的技术也同样适用于 min() 和 max() 等函数。比如：
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
