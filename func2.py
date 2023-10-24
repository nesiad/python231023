# func2.py
#스코핑룰(LGB규칙)
x = 1
def func1(a):
    return a+x

#호출
print(func1(1))

def func2(a):
    x = 5
    return a+x

#호출
print(func2(1))

#기본값이 있는 경우
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

#키워드인자방식(매개변수명을 기술하는 경우)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("multi.com", "80"))
print(connectURI(port="8080", server="multi.com"))

#가변인자:가변적인 상황(* Tuple의미)
def union(*ar):
    #지역변수
    result = []
    #HAM(0) | SPAM(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            #만약에 x가 result에 없다면
            if x not in result:
                result.append(x)
    return result

#호출(디버깅할 때 중단점-Break Point)
print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))

#람다(한줄로 기술하는 즉흥적인, 일회성 함수)
g = lambda x,y:x*y
print(g(3,4))

print( (lambda x:x*x)(3) )

print( globals() )