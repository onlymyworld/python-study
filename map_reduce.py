# map 的第一个参数是函数，第二个参数是iterable;
# 假如我们要将一个f(x)= x*x;作用于一个list[1,2,3,4,5,6,7,8];我们可以这样做

# 先定义给函数
def f(x):
	return x*x

r= map(f,[1,2,3,4,5,6,7,8])
values=list(r)
print(values)
# map传入的第一个参数是r,为函数本身,由于结果r是一个Iterator,Iterator是惰性序列,因此通过list()函数让它把整个序列都计算出来并返回一个list
# 
# 使用另外一种方法实现
L=[]
for n in [1,2,3,4,5,6,7,8]:
	L.append(f(n))
print(L)
# 但是第二中方式要繁琐并且不能很快的看出把f函数作用到了list上面
# map是一种高阶函数。
# 
# reduce
# reduce把一个函数作用在一个序列[x1,x2,x3,x4.....]上，这个函数鼻血接受两个参数,reduce把结果继续和序列的下一个元素做累积计算。
# reduce(fn,[x1,x2,x3]) = f(f(f(x1,x2),x3),x4)

from functool import reduce
def add(x,y):
	return x*y
reduce(add,[1,3,5,7,9])

# 将一个字符串拆分为int并进行后续的操作
from functool import reduce
def add(x,y):
	return x*10+y
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
reduce(add,map(char2num,'13579'))
# 13579运行结果
# 还可以简化为这样
reduce(lambda x,y:x*10+y,map(char2num,'13579'))
