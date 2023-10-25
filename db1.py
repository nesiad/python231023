# db1.py
import sqlite3

#연결객체(일단은 메모리에 저장)
con = sqlite3.connect(":memory:")
#커서객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("""create table if not exists PhoneBook
    (id integer primary key autoincrement, name text, phoneNum text);
    """)

#1건입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('전우치', '010-222');")

#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-333"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);",
    (name, phoneNumber))

#다중으로 행을 입력
datalist = (("박문수", "010-333"), ("김길동", "010-567"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);",
    datalist)

#검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())


