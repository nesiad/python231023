# DemoFormat.py

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---0을 출력---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))


for i in range(1,11):
    url = "http://www.multicampus.com/?page=" + str(i)
    print(url)

print("---서식 지정---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일 쓰기
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#기존 파일에 첨부
f = open("demo.txt", "a+", encoding="utf-8")
f.write("다른 내용을 첨부\n")
f.close()

#파일 읽기
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
#처음으로 리셋
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

f.seek(0)
lst = f.readlines()
for item in lst:
    print(item, end="")

f.close()
