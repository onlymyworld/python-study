# class Fib(object):
# 	def __getitem__(self,n):
# 		if isinstance(n,int):
# 			a,b=1,1
# 			for x in range(n):
# 				a,b=b,a+b
# 			return a
# 		if isinstance(n,slice):
# 			start = n.start
# 			stop = n.stop
# 			if start is None:
# 				start=0
# 			if stop is None:
# 				return "stop is not undefined!" #返回提示stop未定义
# 			a,b=1,1
# 			L=[]
# 			for x in range(stop):
# 				if x>=start:
# 					L.append(a)
# 				a,b=b,a+b
# 			return L
# f = Fib()
# print(f[:10:2])

#
# class Chain(object):
# 	def __init__(self,path=''):
# 		self._path =path
# 	def __getattr__(self,path):
# 		return Chain('%s/%s' % (self._path,path))
# 	def __str__(self):
# 		return self._path
# 	__repr__=__str__
# print(Chain().status.user.timeline.list)
# 

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance,method()来调用,能不能直接在实例
# 本身上调用呢?在Python中,答案是肯定的,任何类,只需要定义一个__call__()方法,就可以直接对实例进行调用,
# class Student(object):
# 	def __init__(self,name):
# 		self.name=name
# 	def __call__(self):
# 		print('My name is %s' % self.name)

# s = Student('Michael')
# print(s())
# __call__()还可以定义参数,对实例进行直接调用就好比对一个函数进行调用一样,所以你完全可以把对象看成
# 函数，把函数看成对象,因为这两者之间本来就没有什么区别
# 
# 
# 
# callable(s)
# callable(max)
# callable('str')
# 
# 
# 通过callable()函数,我们就可以判断一个对象是否是"可调用"对象！
# 
# 
class Student(object):
	@property
	def brith(self):
		return self._brith
	@brith.setter
	def brith(self,value):
		self._brith = value
	$property
	def age(self):
		return 2015 - self._brith

s = Student()
s.brith(1994)
print(s.age())

