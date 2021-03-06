# 使用枚举类
# 
# JAN=1
# FEB=2
# MAR=3
# ...
# 这个好处就是很简单，但是缺点就是类型是int，并且任然是变量
# 更好的办法就是这样的枚举类型定义一个class类型，然后，每个常量
from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# 这样我们就获得了Month类型的枚举类,可以直接使用Month.Jan来引用一个常量,或者枚举它的所有成员：
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
# value属性则是自动赋给成员的int常量,默认从1开始计数。
# 如果需要更精确的控制枚举类型,可以从Enum派生出自定义类
from enum import Enum,unique
@unique
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6

# @unique装饰器可以帮助我们检查保证没有重复值
# 访问这些枚举类型可以有若干种方法
day1=Weekday.Mon
day1
Weekday.Tue
Weekday['Tue']
Weekday.Tue.value 
# 可以用成员名称引用枚举常量,又可以直接根据value的值获得枚举常量
