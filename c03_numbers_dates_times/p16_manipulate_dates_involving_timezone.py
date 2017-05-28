# -*- coding:utf-8 -*-

# 问题
# 你有一个安排在2012年12月21日早上9:30的电话会议，地点在芝加哥。 而你的朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？

# 解决方案
# 对几乎所有涉及到时区的问题，你都应该使用 pytz 模块。这个包提供了Olson时区数据库， 它是时区信息的事实上的标准，在很多语言和操作系统里面都可以找到。

# pytz 模块一个主要用途是将 datetime 库创建的简单日期对象本地化。 比如，下面如何表示一个芝加哥时间的示例：
from datetime import datetime, timedelta
from pytz import timezone
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)  # 2012-12-21 09:30:00

# Localize the date for Chicago
shanghai = timezone('Asia/Shanghai')
loc_d = shanghai.localize(d)
print(loc_d)  # 2012-12-21 09:30:00+08:00

# 一旦日期被本地化了， 它就可以转换为其他时区的时间了。 为了得到班加罗尔对应的时间，你可以这样做：
tokyo_d = loc_d.astimezone(timezone('Asia/Tokyo'))
print(tokyo_d)  # 2012-12-21 10:30:00+09:00

# 如果你打算在本地化日期上执行计算，你需要特别注意夏令时转换和其他细节。
# 比如，在2013年，美国标准夏令时时间开始于本地时间3月13日凌晨2:00(在那时，时间向前跳过一小时)。
# 如果你正在执行本地计算，你会得到一个错误。比如：
d = datetime(2013, 3, 10, 1, 45)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)  # 2013-03-10 01:45:00-06:00
later = loc_d + timedelta(minutes=30)
print(later)  # 2013-03-10 02:15:00-06:00  #WRONG!

# 结果错误是因为它并没有考虑在本地时间中有一小时的跳跃。 为了修正这个错误，可以使用时区对象 normalize() 方法。比如：
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)  # 2013-03-10 03:15:00-05:00

# 讨论
# 为了不让你被这些东东弄的晕头转向，处理本地化日期的通常的策略先将所有日期转换为UTC时间， 并用它来执行所有的中间存储和操作。比如：


