# 使用@property

# 在绑定属性时,我们直接把属性暴露出去,虽然看起来很简单,但是没办法
# 检查参数,导致可以把成绩随便改：
# s = Student()
# s.score = 99999
# 这种修改方式就是不合理的。
# 这显然不合逻辑,为了现在score的范围,可以通过一个set_score()方法来设置成绩,在通过一个get_score()来获取成绩,这样
# 在set_score方法里,就可以检查参数
# 
# 
# 
# 
# class Student(object):
# 	def get_score(self):
# 		return self._score
# 	def set_score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer!')
# 		if value <0 or value > 100:
# 			raise ValueError('score must between 0~100!')
# 		self._score = value

# s = Student()
# s.set_score(1000)
# print(s.get_score())
# 
# 
# 
# 但是对于上面的调用方法来说，还是过于复杂，没有直接调用属性那么直接简单
# 有没有既能检查参数,又可以用类似属性这样简单的方式来访问类的变量呢？
# 装饰器(decorator)可以给函数动态加上功能，对于类的方法，装饰器一样起作用,Python内置的@property装饰器就是负责把
# 一个方法变成属性调用的。

# class Student(object):
# 	@property
# 	def score(self):
# 		return self._score
# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer!')
# 		if value <0 or value > 100:
# 			raise ValueError('score must between 0-100!')
# 		self._score = value

# s = Student()
# s.score =999
# print(s.score)


# @property的实现比较复杂,我们先考察如何使用,把一个getter方法变成属性,只需要加上@property就可以了,此时
# @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值,于是我们就拥有了一个可控
# 的属性操作


# 注意到这个神奇的@property，我们在对实例属性操作的时候,就知道该属性很可能不是直接暴露,而是通过getter和setter方法
# 来实现的
# 如何定义一个只读属性呢？只定义getter方法,而不定义setter方法就是一个只读属性

class Student(object):
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value
	@property
	def age(self):
		return 2017-self._birth

s = Student()
s.birth = 1994
print(s.age)
# 上面的birth是可读写属性,而age就是一个只读属性,因为age可以根据birth和当前时间来计算
# 