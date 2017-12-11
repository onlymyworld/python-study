from collections import Iterable
import os
# 迭代
d = {"a":1,"b":2,"c":3}
for key in d:
	print(key)

for v in d.values():
	print(v)

isinstance('abc',Iterable); #true
isinstance('123',Iterable); #true
isinstance(123,Iterable); #false

for i, value in enumerate(['A','B','C']):
	print(i,value)

for x, y in [(1,1),(2,4),(3,9)]:
	print(x,y)

l=[];
for x in range(1,10):
	l.append(x*x)

print(l);

