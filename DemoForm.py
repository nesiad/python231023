# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]
#폼 클래스 정의
class DemoForm(QDialog, form_class): #다중상속 허용
    #초기화 메서드
    def __init__(self):
        super().__init__() #다중상속시 부모들의 생성자 동시 호출을 간단하게 표현
        self.setupUi(self)
        self.label.setText("첫번째 화면 보여주기~~")
#직접 실행했는지 여부(진입점 체크)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec()



