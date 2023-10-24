class Person:
    def __init__(self, id, phoneNumber):
        self.id = id  # 개인의 ID
        self.phoneNumber = phoneNumber  # 개인의 전화번호

    def printInfo(self):
        print(f"ID: {self.id}")
        print(f"전화번호: {self.phoneNumber}")

class Manager(Person):
    def __init__(self, id, phoneNumber, skill):
        super().__init__(id, phoneNumber)
        self.skill = skill  # 관리자의 스킬

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 메서드 호출
        print(f"스킬: {self.skill}")

class Employee(Manager):
    def __init__(self, id, phoneNumber, skill, title):
        super().__init__(id, phoneNumber, skill)
        self.title = title  # 직원의 직책

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 메서드 호출
        print(f"직책: {self.title}")

# 클래스의 사용 예시:
person1 = Person(id=1, phoneNumber="123-456-7890")
person1.printInfo()

manager1 = Manager(id=2, phoneNumber="987-654-3210", skill="리더십")
manager1.printInfo()

employee1 = Employee(id=3, phoneNumber="555-123-4567", skill="프로그래밍", title="소프트웨어 엔지니어")
employee1.printInfo()
