import tkinter as tk
from tkinter import font
from DBHelper import *
from Function import *
class Teacher_main:
    def __init__(self,Teacher):
        tea_info = "工号：{} ,姓名：{}，性别：{}".format( Teacher.id,  Teacher.name, Teacher.sex)
        self.teacher = Teacher
        self.id = Teacher.id
        self.name = Teacher.name
        self.sex  = Teacher.sex
        self.root = tk.Tk()
        self.large_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.custom_font = font.Font(family="Helvetica", size=12)
        self.tea_info_label = tk.Label(self.root, text=tea_info, font=self.large_font)
        self.time = '2024-5-12'
        self.time_label = tk.Label(self.root, text="当前时间：" + self.time, font=self.custom_font)
        self.frame = tk.Frame(self.root)
        self.label = tk.Label(self.root, text="授课课程：", font=self.custom_font)
        self.menubar = tk.Menu(self.root)
        self.frame = tk.Frame(self.root)

        self.initwindow()
    def initwindow(self):
        self.root.geometry("1000x600+200+200")
        self.root.title("教师界面")
        self.time_label.pack(side="top", fill="x")
        self.tea_info_label.pack(padx=20, pady=50)

        # 菜单,用来重新登录
        self.set_menu()
        # listbox用来显示授课课程
        self.set_listbox()
        # 添加按钮，实现功能
        self.set_btn_function()

        self.root.mainloop()
    def set_btn_function(self):
        btn_hasset_job = tk.Button(self.frame, text="作业提交状态", font=self.custom_font, command=self.view_hasset_job)
        btn_hasview_job = tk.Button(self.frame, text="作业查看状态", font=self.custom_font, command=self.view_hasview_job)

        btn_hasset_job.pack(side=tk.LEFT, padx=10, pady=10)
        btn_hasview_job.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame.pack(expand=True)  # 使用 expand=True 使 Frame 在主窗口中居中
    def set_menu(self):
        # 菜单,用来重新登录
        # 创建一个文件菜单项，并添加一些子菜单项
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="退出", command=self.back)
        self.menubar.add_cascade(label="选项", menu=file_menu)
        # 显示菜单栏
        self.root.config(menu=self.menubar)
    def set_listbox(self):
        # listbox用来显示授课课程
        listbox = tk.Listbox(self.root, width=40, height=10, font=("Helvetica", 12))  # 在初始化方法中定义 listbox
        listbox.pack(side=tk.BOTTOM, padx=20, pady=20)
        # 绑定点击事件
        listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

        self.label.pack(side=tk.BOTTOM, padx=20, pady=30)

        id,items = self.get_class_items(self.name)
        self.course = items
        self.course_id = id
        print(items)
        # 将列表中的所有项目添加到 Listbox 中
        for item in items:
            listbox.insert(tk.END, item)

    def on_listbox_select(self,event):
        # 获取当前选中的项
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            id,name = self.course_id[index],self.course[index]
            self.add_job_window(id,name)
    def add_job_window(self,cid,cname):
        new_window = tea_assign_job(cid,cname,self.id)

    def view_hasset_job(self):
        db = DBHelper()
        ans = db.get_tea_hasset_job(self.id,self.time)
        gth = tea_view_hasset_job(ans,self.id)
        db.close()
    def view_hasview_job(self):
        db = DBHelper()
        ans = db.get_tea_hasset_job(self.id,self.time)
        gth = tea_view_hasview_job(ans, self.id)
        db.close()
    def get_class_items(self,name):
        db = DBHelper()
        id,name = db.get_tea_class(name)
        db.close()
        return id,name
    def back(self):
        self.root.destroy()
