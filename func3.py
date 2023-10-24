#필터링하는 함수
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링하는 경우---")
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

#람다함수 적용
print("---람다함수---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

#분기구문
#선택한 블럭 주석: ctrl + /
# score = int(input("점수를 입력:"))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

#반복문
value = 5
while value > 0:
    print(value)
    value -= 1


lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)

#수열 함수
lst = list(range(1,11))
print(lst)
print("---break구문---")
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2:
        continue
    print("Item:{0}".format(i))

print("---수열함수---")
print(list(range(2000,2024)))
print(list(range(1,32)))

for i in range(5):
    print(i)

print("---리스트 함축---")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
fruits = ("apple", "orange", "kiwi")
print([len(i) for i in fruits])