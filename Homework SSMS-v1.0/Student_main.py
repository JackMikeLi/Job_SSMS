import tkinter as tk
from tkinter import font
from DBHelper import *
from Function import *
class Student_main:
    def __init__(self,stu,menu):
        stu_info = "学号：{} ,姓名：{}，性别：{}，年龄：{}，专业：{}，班级号：{}".format(stu.id,stu.name,stu.sex,stu.age,stu.major,stu.sc_num)
        self.menu = menu
        self.do_have = False
        self.student = stu
        self.id = stu.id
        self.name = stu.name
        self.flag = 0
        self.root = tk.Tk()  # 创建主窗口
        self.large_font = font.Font(family="Helvetica", size=15, weight="bold")
        self.custom_font = font.Font(family="Helvetica", size=12)
        self.stu_info_label = tk.Label(self.root, text= stu_info, font=self.large_font)
        self.time = '2024-5-12'
        self.time_label = tk.Label(self.root,text="当前时间：" + self.time,font =self.custom_font)
        self.label_class = tk.Label(self.root,text="已选课程：",font=self.custom_font)
        self.menubar = tk.Menu(self.root)
        self.frame = tk.Frame(self.root)
        self.initwindow()
    def initwindow(self):
        self.root.geometry("1000x600+200+200")
        self.root.title("学生界面")
        self.time_label.pack(side="top", fill="x")
        self.stu_info_label.pack(padx=20, pady=50)

        # 创建一个文件菜单项，并添加一些子菜单项
        self.set_menu()

        #设置已选课程的listbox
        self.set_listbox()

        #添加按钮
        self.set_btn_function()

        self.do_has_oneday_job()
        self.root.mainloop()
    def do_has_oneday_job(self):
        db = DBHelper()
        ans = db.do_stu_oneday_job(self.id)
        if ans != []:
            self.do_have = True
            message = "您的作业：{}还有一天截止，请尽快提交!".format(ans)
            messagebox.showinfo('作业快截止了！',message)
        db.close()
    def set_menu(self):
        # 菜单,用来重新登录
        # 创建一个文件菜单项，并添加一些子菜单项
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="退出", command=self.back)
        self.menubar.add_cascade(label="选项", menu=file_menu)
        # 显示菜单栏
        self.root.config(menu=self.menubar)
    def set_btn_function(self):
        #添加按钮
        btn_view_all = tk.Button(self.frame, text="查看所有课程", font=self.custom_font, command=self.view_all)
        btn_should_sub = tk.Button(self.frame, text="我的作业", font=self.custom_font, command=self.Job_Now)

        btn_view_all.pack(side=tk.LEFT, padx=10, pady=10)
        btn_should_sub.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame.pack(expand=True)  # 使用 expand=True 使 Frame 在主窗口中居中


    def set_listbox(self):
        # listbox用来显示已选课程
        listbox_1 = tk.Listbox(self.root, width=40, height=10, font=("Helvetica", 12))  # 在初始化方法中定义 listbox
        listbox_1.pack(side=tk.BOTTOM, padx=20, pady=20)
        self.label_class.pack(side=tk.BOTTOM, padx=20, pady=30)
        items = self.get_class_items()
        print(items)
        # 将列表中的所有项目添加到 Listbox 中
        for item in items:
            listbox_1.insert(tk.END, item)
        # 绑定 Listbox 的点击事件
         # 绑定 Listbox 的点击事件
        listbox_1.bind("<<ListboxSelect>>", self.on_listbox_click)

        # 保存 listbox 供后续使用
        self.listbox_1 = listbox_1

    def on_listbox_click(self, event):
        # 获取被点击项的索引
        selected_index = self.listbox_1.curselection()
        if selected_index:
            # 获取被点击项的文本
            self.row_index = selected_index[0]
            self.tid = self.Tid[self.row_index]
            ans = self.get_class_info()
            window = stu_view_tea_hasset_job(ans,self.id,self.Tid[self.row_index])
    def get_class_info(self):
        db = DBHelper()
        ans = db.get_tea_hasset_job(self.tid, self.time)
        db.close()
        return ans
    def view_all(self):
        db = DBHelper()
        Courses = db.courses_info()
        sid = self.id
        view = View_stu_takecourse_treeview(Courses)
        db.close()
    def Job_Now(self):
        db = DBHelper()
        job = db.get_stu_should_sub(self.name, self.time)
        JN = Stu_Job_now_treeview(job,self.id)
        db.close()
    def getflag(self):
        return self.flag
    def get_class_items(self):
        db = DBHelper()
        cid,cname,tid = db.get_stu_class(self.id)
        self.Cid = cid
        self.Cname = cname
        self.Tid = tid
        db.close()
        return cname
    def back(self):
        self.root.destroy()
        #self.menu.__init__()#用于重新登录,暂未完成




