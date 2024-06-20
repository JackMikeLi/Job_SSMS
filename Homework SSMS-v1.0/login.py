from loginHelper import *
from Student_main import *
from Teacher_main import *
from Manager_main import *
class Login:
    def __init__(self):
        self.menu = identity()
        self.flag = self.menu.getflag()
        self.login()
    def login(self):
        if(self.flag == 1):
            self.student_login()
        elif(self.flag == 2):
            self.teacher_login()
        elif(self.flag ==3):
            self.manager_login()
    def student_login(self):
        print("学生登录")
        stu = self.menu.getinfo()
        stu.show_info()
        stu_main = Student_main(stu, self.menu)
    def teacher_login(self):
        print("老师登录！")
        tea = self.menu.getinfo()
        tea.show_info()
        tea_main = Teacher_main(tea)
    def manager_login(self):
        print("管理员登录")
        dba = Manager_main()
login = Login()

