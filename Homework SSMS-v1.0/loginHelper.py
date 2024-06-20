import tkinter as tk
from tkinter import messagebox
from tkinter import font
from DBHelper import *
from table import Student,Teacher
class student_login:
    def __init__(self):
        self.student = Student()
        self.root = tk.Tk()
        self.custom_font = font.Font(family="Helvetica", size=20)
        self.label_id = tk.Label(self.root, text="学号",font=self.custom_font)
        self.label_name = tk.Label(self.root, text="姓名",font=self.custom_font)
        self.entry_id = tk.Entry(self.root,width=20)
        self.entry_name = tk.Entry(self.root,width=20)
        self.btn_login = tk.Button(self.root, text="登录",font=self.custom_font, command=self.login)
        self.btn_back = tk.Button(self.root, text="返回",font=self.custom_font, command=self.back)
        self.initwindow()

    def initwindow(self):
        root = self.root
        label_id = self.label_id
        label_name = self.label_name
        entry_id = self.entry_id
        entry_name = self.entry_name
        btn_login = self.btn_login
        btn_back = self.btn_back

        root.title("学生登录窗口")
        root.geometry("300x600+200+100")
        # 创建用户名标签和文本框，使用 grid() 函数水平放置
        label_id.grid(row=0, column=0, padx=10, pady=5)  # 放置在第一行第一列，设置边距
        entry_id.grid(row=0, column=1, padx=25, pady=5)  # 放置在第一行第二列，设置边距

        # 创建密码标签和文本框，使用 grid() 函数水平放置
        label_name.grid(row=1, column=0, padx=10, pady=5)  # 放置在第二行第一列，设置边距
        entry_name.grid(row=1, column=1, padx=25, pady=5)  # 放置在第二行第二列，设置边距

        # 创建登录按钮，使用 grid() 函数放置在第三行中间
        btn_login.grid(row=2, column=0, padx=10, pady=20)  # 跨两列放置，设置边距
        btn_back.grid(row=2, column=1,padx=10, pady=20)

        self.root.mainloop()
    def login(self):
        db = DBHelper()
        id, name, sex, age, major, sc_num = db.stu_info()
        input_id = self.entry_id.get()
        input_name = self.entry_name.get()

        if input_id in id:
            index = id.index(input_id)
            if input_name == name[index]:
                # messagebox.showinfo("登录成功", "欢迎回来，{}".format(input_name))
                self.student = Student(id[index],name[index],sex[index],age[index],major[index],sc_num[index])
                self.root.destroy()
            else:
                messagebox.showerror("登录失败", "学号或姓名输入错误")
        db.close()
    def getinfo(self):
        return self.student
    def back(self):
        self.root.destroy()
        identity()
class teacher_login:
    def __init__(self):
        self.teacher = Teacher()
        self.root = tk.Tk()  # 创建主窗口
        self.custom_font = font.Font(family="Helvetica", size=20)
        self.label_id = tk.Label(self.root, text="工号",font=self.custom_font)
        self.label_name = tk.Label(self.root, text="姓名",font=self.custom_font)
        self.entry_id = tk.Entry(self.root,width=20)
        self.entry_name = tk.Entry(self.root,width=20)
        self.btn_login = tk.Button(self.root, text="登录",font=self.custom_font, command=self.login)
        self.btn_back = tk.Button(self.root, text="返回",font=self.custom_font, command=self.back)
        self.initwindow()

    def initwindow(self):
        root = self.root
        label_id = self.label_id
        label_name = self.label_name
        entry_id = self.entry_id
        entry_name = self.entry_name
        btn_login = self.btn_login
        btn_back = self.btn_back

        root.title("教师登录窗口")
        root.geometry("300x600+200+100")
        # 创建用户名标签和文本框，使用 grid() 函数水平放置
        label_id.grid(row=0, column=0, padx=10, pady=5)  # 放置在第一行第一列，设置边距
        entry_id.grid(row=0, column=1, padx=25, pady=5)  # 放置在第一行第二列，设置边距

        # 创建密码标签和文本框，使用 grid() 函数水平放置
        label_name.grid(row=1, column=0, padx=10, pady=5)  # 放置在第二行第一列，设置边距
        entry_name.grid(row=1, column=1, padx=25, pady=5)  # 放置在第二行第二列，设置边距

        # 创建登录按钮，使用 grid() 函数放置在第三行中间
        btn_login.grid(row=2, column=0, padx=10, pady=20)  # 跨两列放置，设置边距
        btn_back.grid(row=2, column=1, padx=10, pady=20)
        # 运行主循环
        root.mainloop()
    def getinfo(self):
        return self.teacher
    def login(self):
        db = DBHelper()
        id, name , sex = db.tea_info()
        input_id = self.entry_id.get()
        input_name = self.entry_name.get()

        # 假设用户名和密码为固定值
        if input_id in id:
            index = id.index(input_id)
            if input_name == name[index]:
                # messagebox.showinfo("登录成功", "欢迎回来，{}".format(input_name))
                self.teacher = Teacher(id[index], name[index], sex[index])
                self.root.destroy()
            else:
                messagebox.showerror("登录失败", "工号或姓名输入错误")
        db.close()
    def back(self):
        self.root.destroy()
        identity()
class manager_login:
    def __init__(self):
        self.root = tk.Tk()  # 创建主窗口
        self.custom_font = font.Font(family="Helvetica", size=20)
        self.label_id = tk.Label(self.root, text="密钥",font=self.custom_font)
        self.label_name = tk.Label(self.root, text="姓名",font=self.custom_font)
        self.entry_id = tk.Entry(self.root,width=20)
        self.entry_name = tk.Entry(self.root,width=20)
        self.btn_login = tk.Button(self.root, text="登录",font=self.custom_font, command=self.login)
        self.btn_back = tk.Button(self.root, text="返回",font=self.custom_font, command=self.back)
        self.initwindow()

    def initwindow(self):
        root = self.root
        label_id = self.label_id
        label_name = self.label_name
        entry_id = self.entry_id
        entry_name = self.entry_name
        btn_login = self.btn_login
        btn_back = self.btn_back

        root.title("DBA窗口")
        root.geometry("300x600+200+100")
        # 创建用户名标签和文本框，使用 grid() 函数水平放置
        label_id.grid(row=0, column=0, padx=10, pady=5)  # 放置在第一行第一列，设置边距
        entry_id.grid(row=0, column=1, padx=25, pady=5)  # 放置在第一行第二列，设置边距

        # 创建密码标签和文本框，使用 grid() 函数水平放置
        label_name.grid(row=1, column=0, padx=10, pady=5)  # 放置在第二行第一列，设置边距
        entry_name.grid(row=1, column=1, padx=25, pady=5)  # 放置在第二行第二列，设置边距

        # 创建登录按钮，使用 grid() 函数放置在第三行中间
        btn_login.grid(row=2, column=0, padx=10, pady=20)  # 跨两列放置，设置边距
        btn_back.grid(row=2, column=1, padx=10, pady=20)  # 跨两列放置，设置边距
        # 运行主循环
        root.mainloop()
    def login(self):
        id = '999'
        name = 'DBA'
        input_id = self.entry_id.get()
        input_name = self.entry_name.get()

        # 假设用户名和密码为固定值
        if input_id == id and input_name == name:
            # messagebox.showinfo("登录成功", "欢迎回来，{}".format(input_name))
            self.root.destroy()
        else:
            messagebox.showerror("登录失败", "密钥或姓名错误")
    def back(self):
        self.root.destroy()
        menu = identity()

class identity():
    def __init__(self):
        self.root = tk.Tk()
        self.flag = 0
        self.student = Student()
        self.teacher = Teacher()
        self.button_font = font.Font(family='Helvetica', size=20, weight='bold')
        self.button1 = tk.Button(self.root, text='学生登录', command=self.on_button1_click, font=self.button_font)
        self.button2 = tk.Button(self.root, text='教师登录', command=self.on_button2_click, font=self.button_font)
        self.button3 = tk.Button(self.root, text='管理员登录', command=self.on_button3_click, font=self.button_font)
        self.initwindow()
    def initwindow(self):
        self.root.title("作业提交综合管理系统 v.1.0")
        self.root.geometry("500x500+200+100")
        button_font = self.button_font
        button1 = self.button1
        button2 = self.button2
        button3 = self.button3

        button1.pack(fill=tk.BOTH, expand=True)
        button2.pack(fill=tk.BOTH, expand=True)
        button3.pack(fill=tk.BOTH, expand=True)
        self.root.mainloop()
    def getflag(self):
        return self.flag
    def on_button1_click(self):
        self.root.destroy()
        self.flag = 1
        print(self.flag)
        menu = student_login()
        stu = menu.getinfo()
        self.student = stu #这一句很重要！！！
    def on_button2_click(self):
        self.root.destroy()
        self.flag = 2
        print(self.flag)
        menu = teacher_login()
        tea = menu.getinfo()
        self.teacher = tea #这一句很重要！！！

    def on_button3_click(self):
        self.root.destroy()
        self.flag = 3
        print(self.flag)
        menu = manager_login()
    def getinfo(self):
        if(self.flag == 1):
            return self.student
        elif(self.flag == 2):
            return self.teacher
    def getflag(self):
        return self.flag
class Version():
    def __init__(self):
        self.root = tk.Tk()
        self.flag = 0
        self.student = Student()
        self.teacher = Teacher()
        self.frame = tk.Frame(self.root)
        self.initwindow()
    def initwindow(self):
        self.root.title("DBA作业综合管理系统")
        self.root.geometry("500x500+200+100")
        self.set_frame()
        self.root.mainloop()
    def set_frame(self):
        self.custom_font = font.Font(family="Helvetica", size=20)
        self.label = tk.Label(self.frame,text = "作业综合管理系统 v.1.0",font = self.custom_font)
        self.label.pack(side = tk.TOP,padx=5, pady=5)

        self.button_font = font.Font(family='Helvetica', size=20, weight='bold')
        self.button = tk.Button(self.frame, text='启动！', command=self.on_button_click, font=self.button_font)
        self.button.pack(fill=tk.BOTH,padx=5, pady=5)

        self.frame.pack(expand=True,padx=5, pady=5, fill=tk.BOTH)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    def getflag(self):
        return self.flag
    def on_button_click(self):
        self.root.destroy()
        self.menu = identity()
        self.flag = self.menu.getflag()