s = "中国人"

print(type(s))
print(len(s))
print(isinstance(s,str))
print('{0:.6f}'.format(1/3))

test = "apple, banana,orange,peach"
a = test.find("banana")
print(a)
b = test.rfind('a')
print(b)
print(len(test))
print(test.count('a'))
print(test.split(',',maxsplit=1))
print(test.rsplit(','))
print(len(test.partition(',')))
print(test.partition(','))
li = ["a","b","c"]
sep = ','
print(type(sep.join(li)))