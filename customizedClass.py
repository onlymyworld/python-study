# 定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意
# 这些在Python中是有特殊用途的,
# __slots__我们已经知道怎么用了,__len__()方法我们也知道是为了让class
# 作用于len()函数
# 除此之外，Python的class中还有许多这样特殊用途的函数，可以帮助我们定制类
# __str__
class Student(object):
	def __init__(self,name):
		self.name = name
print(Student('Michael'))
# 打印出来是这样，<__main__.Student object at 0x0000000001E5E9E8> 
# 是不是感觉不好看
# 怎么才能打印得更好看呢，只需要定义好__str__()方法，返回一个好看的字符串就ok了
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name:%s)' % self.name

print(Student('Michael'))
# 打印出来的效果是这样的,Student object (name:Michael)
s = Student('Michael')
s
# 这样打印出来的效果是这样 <__main__.Student object at 0x0000000001E5E9B0>，还是最初的那样
# 而不是使用的__str__的方法
# 这是因为直接显示变量调用的不是__str__(),而是__repr__(),两者的区别是__str__()返回用户看到的字符串,
# 而__repr__()返回程序开发者看到的字符串,也就是说,__repr__()是为了调试服务
# 解决办法是再定义一个__repr__(),但是通常__str__()和__repr__()代码是一样的，所有可以直接用__repr__ = __str__
# 的方式解决问题
class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name=%s)' % self.name
	__repr = __str__


# __iter__
# 如果一个类想被用于for ... in 循环，类似list或tuple那样,就必须实现一个__iter__()方法,该方法返回一个迭代对象,
# 然后,Python的for循环就会不断调用该迭代对象的__next__()方法,拿到循环的下一个值,
# 直到遇到StopIteration错误时退出循环。
# 我们以斐波那契数列为例,写一个Fib类,可以作用于for循环:
 class Fib(object):
 	def __init__(self):
 		self.a,self.b = 0,1 #初始化两个计数器a,b
 	def __iter__(self):
 		return self #实例本身就是迭代对象,故返回自己
 	def __next__(self):
 		self.a,self.b = self.b,self.a+self.b #计算下一个值
 		if self.a > 100000: #退出循环条件
 			raise StopIteration()
 		return self.a #返回下一个值
 # 现在,试一试把Fib实例作用于for循环
  for n in Fib():
  	 print(n)

 # __getitem__
 # Fib实例虽然能作用于for循环,看起来和list有点像,但是,把它当成list来使用还是不行,比如,取第五个元素
 Fib()[5]
 # >>> Fib()[1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing
# 会出现上述的错误，
# 要表现得像list那样按照下标取出元素,需要实现__getitem__()方法:
# 
class Fib(object):
	def __getitem__(self,n):
		a,b=1,1
		for x in range(n):
			a,b=b,a+b
		return a
# 现在测试一个例子,现在就可以按下标访问数列的任意一项了:
f=Fib()
f[5]
# 但是list有个神奇的切片方法:
list(range(100))[5:100]
# >>>[5,6,7,8,9]
# 对于Fib报错,原因是__getitem__()传入的参数可能是int,也可能是一个切片对象slice,所以在接到参数要做判断
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start=0
			if stop is None:
				return 'Stop is not undefined!'
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b
			return L
f = Fib()
print(f[0:5])

