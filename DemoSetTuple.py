# DemoSetTuple.py
#세트형식으로 초기화
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
#print( a[0] )

print("---Tuple형식---")
tp = (1,2,3)
print(tp)
print(len(tp))
print(tp[0])
print("id: %s, name: %s" % ("kim","김유신"))

#함수 정의
def calc(a,b):
    return a+b, a*b
#함수 호출
print(calc(3,4))

