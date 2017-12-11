# 获取对象信息
# 使用type
type(123)
type('str')
type(None)

# 指向函数或者是类
type(abs)

type(123) == type(456)
type(123) == int
type('abc') == type('123')
type('abc') ==str
type('abc') == type(123)

# 判断基本数据类型可以直接写int,str等,但如果判断一个对象是否为函数怎么办？
# 可以使用types模块中定义的常量
import types
def fn():
	pass
type(fn) ==types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lamdba x:x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

# 对于class的继承关系来说,使用type()就很不方便。
# 我们要判断class的类型,可以使用isinstance()函数
a = Animal()
d = Dog()
h = Husky()
isinstance(h,Husky)
isinstance(h,Dog)
isinstance(h,Animal)
isinstance(d,Dog) and isinstance(d,Animal)
isinstance(d,Husky)
# 能用type()判断的基本类型也可以用isinstance()判断
isinstance('a',str)
isinstance(123,int)
isinstance(b'a',bytes)

# 判断一个变量是否是某些类型中的一种，比如下面的代码可以判断是否为list或者tuple
isinstance([1,2,3],(list,tuple))
isinstance((1,2,3),(list,tuple))

# 使用dir()
# 获取一个对象的属性和方法
dir("ABC")
len('ABC')
'ABC'.__len__()
# 给自定义类加len方法
class MyDog(object):
	def __len__(self):
		return 100
dog=MyDog()
len(dog)
# 配合getattr(),setattr(),hasattr()方法
# 我们可以直接操作一个对象的状态
class MyObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x

obj=MyObject()

hasattr(obj,'x')
obj.x
hasattr(obj,'y')
setattr(obj,'y','11')
hasattr(obj,'y')
getattr(obj,'y')
obj.y

# 如果视图获取一个不存在的属性,则会抛出错误
getattr(obj,'z')
#传入一个default参数，如果属性不存在，就返回默认值
getattr(obj,'z',404)

# 获取对象的方法
hasattr(obj,'power')
getattr(obj,'power')
fn = getattr(obj,'power')
fn
fn()

