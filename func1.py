# func1.py
#함수 정의
def setValue(newValue):
    #지역변수 초기화
    x = newValue
    print(x)

#함수 호출
setValue(5)

#값을 리턴하는 함수
def swap(x,y):
    return y,x

#함수 호출
result = swap(5,6)
print(result)
