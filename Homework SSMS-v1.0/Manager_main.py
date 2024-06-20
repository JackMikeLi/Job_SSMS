from DBHelper import *
from tkinter import ttk
from tkinter import font
import tkinter as tk
class Manager_main:
    def __init__(self):
        self.root = tk.Tk()
        self.time = '2024-5-12'
        self.custom_font = font.Font(family="Helvetica", size=12)
        self.frame = tk.Frame(self.root)
        self.initwindow()
    def initwindow(self):
        self.root.geometry("500x400+200+200")
        self.root.title("DBA界面")
        self.set_frame()
        self.db = DBHelper()

        self.set_btn()
        self.root.mainloop()
    def set_frame(self):
        self.set_btn()
        self.frame.pack(expand=True,padx=5, pady=5, fill=tk.BOTH)
    def set_btn(self):
        self.btn_student = tk.Button(self.frame, text='学生信息', font=self.custom_font,command=self.btn_student)
        self.btn_student.pack(padx=5, pady=5)

        self.btn_teacher = tk.Button(self.frame, text='教师信息', font=self.custom_font,command=self.btn_teacher)
        self.btn_teacher.pack(padx=5, pady=5)

        self.btn_courses = tk.Button(self.frame, text='课程信息', font=self.custom_font,command=self.btn_courses)
        self.btn_courses.pack(padx=5, pady=5)

        self.btn_sc = tk.Button(self.frame, text='班级信息', font=self.custom_font,command=self.btn_sc)
        self.btn_sc.pack(padx=5, pady=5)

        self.btn_takeclass = tk.Button(self.frame, text='选课信息', font=self.custom_font,command=self.btn_takeclass)
        self.btn_takeclass.pack(padx=5, pady=5)

        self.btn_teaching = tk.Button(self.frame, text='授课信息', font=self.custom_font,command=self.btn_teaching)
        self.btn_teaching.pack(padx=5, pady=5)

        self.btn_job = tk.Button(self.frame, text='作业信息', font=self.custom_font,command=self.btn_job)
        self.btn_job.pack(padx=5, pady=5)

        self.btn_job_submit = tk.Button(self.frame, text='提交作业信息', font=self.custom_font,command=self.btn_job_submit)
        self.btn_job_submit.pack(padx=5, pady=5)

        self.btn_job_view = tk.Button(self.frame, text='作业查看信息', font=self.custom_font,command=self.btn_job_view)
        self.btn_job_view.pack(padx=5, pady=5)

    def btn_student(self):
        res = self.db.stu_info()
        window = tk.Tk()
        window.title('学生表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("id", "name", "sex","age","major","sc"), show="headings")
        self.tree.heading("id", text="学号")
        self.tree.heading("name", text="姓名")
        self.tree.heading("sex", text="性别")
        self.tree.heading("age", text="年龄")
        self.tree.heading("major", text="专业")
        self.tree.heading("sc", text="班级号")

        # 添加示例数据
        data = self.transposed(res)

        for row in data:
            print(row)
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_teacher(self):
        res = self.db.tea_info()
        window = tk.Tk()
        window.title('教师表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("id", "name", "sex"), show="headings")
        self.tree.heading("id", text="工号")
        self.tree.heading("name", text="姓名")
        self.tree.heading("sex", text="性别")

        # 添加示例数据
        data = self.transposed(res)

        for row in data:
            print(row)
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_courses(self):
        res = self.db.courses_info()
        window = tk.Tk()
        window.title('课程表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("id", "name", "sc"), show="headings")
        self.tree.heading("id", text="课程号")
        self.tree.heading("name", text="课程名")
        self.tree.heading("sc", text="班级号")

        # 添加示例数据
        data = res

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_sc(self):
        res = self.db.sc_info()
        window = tk.Tk()
        window.title('班级表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("sc", "sc_count"), show="headings")
        self.tree.heading("sc", text="班级号")
        self.tree.heading("sc_count", text="班级人数")

        # 添加示例数据
        data = res

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_takeclass(self):
        res = self.db.takeclass_info()
        window = tk.Tk()
        window.title('选课表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("sid", "cid"), show="headings")
        self.tree.heading("sid", text="学号")
        self.tree.heading("cid", text="课程号")

        # 添加示例数据
        data = self.transposed(res)

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_teaching(self):
        res = self.db.teaching_info()
        window = tk.Tk()
        window.title('授课表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("tid", "cid"), show="headings")
        self.tree.heading("tid", text="教师工号")
        self.tree.heading("cid", text="课程号")

        # 添加示例数据
        data = self.transposed(res)

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_job(self):
        res = self.db.job_info()
        window = tk.Tk()
        window.title('作业表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("jid", "jname", "jrequire", "jchapter", "jtype","tid","cid", "start", "end", "sc"), show="headings")
        self.tree.heading("jid", text="作业编号")
        self.tree.heading("jname", text="作业名")
        self.tree.heading("jchapter", text="章节信息")
        self.tree.heading("jrequire", text="作业要求")
        self.tree.heading("jtype", text="作业类型")
        self.tree.heading("tid", text="教师编号")
        self.tree.heading("cid", text="课程号")
        self.tree.heading("start", text="开始时间")
        self.tree.heading("end", text="截止时间")
        self.tree.heading("sc", text="班级号")

        # 添加示例数据
        data = self.transposed(res)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(window, orient="horizontal", command=self.tree.xview)
        scrollbar.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=scrollbar.set)

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_job_submit(self):
        res = self.db.Submit_info()
        window = tk.Tk()
        window.title('作业提交表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=( "sid", "jid", "jcontent", "jtime"), show="headings")
        self.tree.heading("sid", text="学号")
        self.tree.heading("jid", text="作业编号")
        self.tree.heading("jcontent", text="作业内容")
        self.tree.heading("jtime", text="提交时间")

        # 添加示例数据
        data = self.transposed(res)

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    def btn_job_view(self):
        res = self.db.View_info()
        window = tk.Tk()
        window.title('作业查看表')
        # 创建Treeview
        self.tree = ttk.Treeview(window, columns=("sid", "jid"), show="headings")
        self.tree.heading("sid", text="学号")
        self.tree.heading("jid", text="作业编号")

        # 添加示例数据
        data = self.transposed(res)


        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def transposed(self,data):
        # 计算总行数
        total_rows = len(data[0])

        # 初始化空列表，用于存储结果
        transposed_data = []

        # 遍历每一行
        for i in range(total_rows):
            # 遍历每一列，并将每列的当前行添加到 transposed_data 中
            transposed_row = []
            for sublist in data:
                transposed_row.append(sublist[i])
            transposed_data.append(transposed_row)

        print(transposed_data)
        return transposed_data

