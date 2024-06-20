import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from DBHelper import *
from tool import *
from table import *
class View_stu_takecourse_treeview:
    def __init__(self,courses):
        self.root = tk.Tk()
        self.courses = courses
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("所有课程")
        self.set_treeview()
    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Sc_id"), show="headings")
        self.tree.heading("ID", text="课程号")
        self.tree.heading("Name", text="课程名")
        self.tree.heading("Sc_id", text="班级号")

        # 添加示例数据
        data = self.courses

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

class View_job_has_submit_treeview:
    def __init__(self,job_hassub):
        self.root = tk.Tk()
        self.job = job_hassub
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("提交的作业")
        self.set_treeview()
    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root, columns=("SName", "J_content", "J_time"), show="headings")
        self.tree.heading("SName", text="学生姓名")
        self.tree.heading("J_content", text="作业内容")
        self.tree.heading("J_time", text="提交时间")

        # 添加示例数据
        data = self.job

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

class View_job_hasnot_submit_treeview:
    def __init__(self,job_hasnotsub):
        self.root = tk.Tk()
        self.job = job_hasnotsub
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("未提交")
        self.set_treeview()
    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root, columns=("SName"), show="headings")
        self.tree.heading("SName", text="学生姓名")
        # 添加示例数据
        data = self.job
        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

class View_job_has_view_treeview:
    def __init__(self,name):
        self.root = tk.Tk()
        self.name = name
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("已查看作业")
        self.set_treeview()
    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root, columns=("SName"), show="headings")
        self.tree.heading("SName", text="学生姓名")

        # 添加示例数据
        data = self.name

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
class View_job_has_notview_treeview:
    def __init__(self,name):
        self.root = tk.Tk()
        self.name = name
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("未查看作业")
        self.set_treeview()
    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root, columns=("SName"), show="headings")
        self.tree.heading("SName", text="学生姓名")

        # 添加示例数据
        data = self.name

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

class Stu_Job_now_treeview:
    def __init__(self,job,sid):
        self.root = tk.Tk()
        self.row_index = -1
        self.sid = sid
        self.job = job
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("我的作业")
        self.set_treeview()
    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root,
                                 columns=("J_id","JName", "JChapter", "JRequire", "JType", 'start_time', 'end_time'),
                                 show="headings")
        self.tree.heading("J_id", text="作业编号")
        self.tree.heading("JName", text="作业名")
        self.tree.heading("JChapter", text="章节信息")
        self.tree.heading("JRequire", text="作业要求")
        self.tree.heading("JType", text="作业类型")
        self.tree.heading("start_time", text="开始时间")
        self.tree.heading("end_time", text="截止时间")

        # 添加示例数据
        data = self.job

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        # 绑定单击事件
        self.tree.bind("<ButtonRelease-1>", self.on_tree_click)

    def on_tree_click(self, event):
        # 获取当前选中的项
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            all_items = self.tree.get_children()
            self.row_index = all_items.index(item_id)
            self.new_window(self.row_index)

    def new_window(self,id):
        job_name = self.job[id][1]
        # 需要判断当前的作业是否提交了

        self.root.destroy()
        self.root2 = tk.Tk()
        self.time = '2024-5-12'
        self.root2.title("提交作业")
        self.custom_font = font.Font(family="Helvetica", size=15)
        self.label_job_name = tk.Label(self.root2,text='作业名',font =self.custom_font)
        self.label_job_name2 = tk.Label(self.root2,text=job_name,font = self.custom_font)
        self.label_job_content = tk.Label(self.root2,text ='作业内容',font=self.custom_font)
        self.entry_job_content = tk.Text(self.root2,width=20,height=20)
        self.label_time = tk.Label(self.root2,text='提交时间',font=self.custom_font)
        self.label_time2 = tk.Label(self.root2,text =self.time,width=20)
        self.btn_submit = tk.Button(self.root2,text='提交',font = self.custom_font,command=self.job_submit)
        self.btn_back = tk.Button(self.root2, text="返回", font=self.custom_font, command=self.back)
        self.set_new_window()
        self.root2.mainloop()
    def Do_submit(self,sid,jid):
        db = DBHelper()
        ans = db.do_stu_submit(sid,jid)
        db.close()
        #True为提交了，False为没提交
        return ans
    def set_new_window(self):
        self.root2.geometry("400x500+100+100")
        # 创建用户名标签和文本框，使用 grid() 函数水平放置
        self.label_job_name.grid(row=0, column=0, padx=10, pady=5)  # 放置在第一行第一列，设置边距
        self.label_job_name2.grid(row=0, column=1, padx=25, pady=5)  # 放置在第一行第二列，设置边距

        self.label_job_content.grid(row=1, column=0, padx=10, pady=5)  # 放置在第一行第一列，设置边距
        self.entry_job_content.grid(row=1, column=1, padx=25, pady=5)  # 放置在第一行第二列，设置边距

        self.label_time.grid(row=2, column=0, padx=10, pady=5)  # 放置在第一行第一列，设置边距
        self.label_time2.grid(row=2, column=1, padx=25, pady=5)  # 放置在第一行第二列，设置边距

        self.btn_submit.grid(padx=20, pady=20)  # 跨两列放置，设置边距
        self.btn_back.grid(padx=20, pady=20)  # 跨两列放置，设置边距

    def job_submit(self):
        #这里需要判断一下是否提交了，如果没提交，则是插入语句，否则则为更新语句
        time = self.time
        sid = self.sid
        jid = self.job[self.row_index][0]
        db = DBHelper()
        job_content = self.entry_job_content.get("1.0", tk.END)
        j_content = getcontent(job_content)
        print(j_content)
        if self.Do_submit(sid,jid):#如果提交了，则更新
            db.stu_update_job(sid,jid,job_content,time)
            messagebox.showinfo('重新提交作业', '更新作业成功！')
        else:#如果没提交，则进行插入
            db.stu_submit_job(sid, jid, j_content, time)
            messagebox.showinfo('提交成功', '成功提交作业！')
        db.close()
        self.root2.destroy()
    def back(self):
        self.root2.destroy()
        self.__init__(self.job,self.sid)


class tea_view_hasset_job:
    def __init__(self, Hasset,tid):
        self.root = tk.Tk()
        self.tid = tid
        self.hasset = Hasset
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("作业提交情况")
        self.set_treeview()

    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root,
                                 columns=("J_id","JName", "JChapter", "JRequire", "JType", 'start_time', 'end_time','sc_id','c_id'),
                                 show="headings")
        self.tree.heading("J_id", text="作业编号")
        self.tree.heading("JName", text="作业名")
        self.tree.heading("JChapter", text="章节信息")
        self.tree.heading("JRequire", text="作业要求")
        self.tree.heading("JType", text="作业类型")
        self.tree.heading("start_time", text="开始时间")
        self.tree.heading("end_time", text="截止时间")
        self.tree.heading("sc_id", text="班级号")
        self.tree.heading("c_id", text="课程号")

        # 添加示例数据
        data = self.hasset

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        # 绑定单击事件
        self.tree.bind("<ButtonRelease-1>", self.on_tree_click)

    def on_tree_click(self, event):
        # 获取当前选中的项
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            all_items = self.tree.get_children()
            self.row_index = all_items.index(item_id)
            self.new_window(self.row_index)
    def new_window(self,id):
        job_name = self.hasset[id][1]
        self.root.destroy()
        self.root2 = tk.Tk()
        self.time = '2024-5-12'
        self.custom_font = font.Font(family="Helvetica", size=15)
        self.label_job_name = tk.Label(self.root2,text=job_name,font = self.custom_font)
        self.btn_view_has_submit = tk.Button(self.root2,text='查看已提交的',font = self.custom_font,command = self.view_has_submit)
        self.btn_view_hasnot_submit = tk.Button(self.root2,text='查看未提交的名单',font = self.custom_font,command = self.view_hasnot_submit)
        self.btn_back = tk.Button(self.root2, text="返回", font=self.custom_font, command=self.back)
        self.set_new_window()
        self.root2.mainloop()
    def set_new_window(self):
        #self.root2.geometry("400x500+100+100")
        self.root2.title("作业信息")
        # 创建用户名标签和文本框，使用 grid() 函数水平放置
        self.label_job_name.grid(row=0, column=0, padx=10, pady=10)
        self.btn_view_has_submit.grid(padx=20, pady=20)  # 跨两列放置，设置边距
        self.btn_view_hasnot_submit.grid(padx=20, pady=20)  # 跨两列放置，设置边距
        self.btn_back.grid(padx=20, pady=20)  # 跨两列放置，设置边距
    def view_has_submit(self):
        jid = self.hasset[self.row_index][0]
        db = DBHelper()
        ans = db.get_job_hassubmit(jid)
        new_window = View_job_has_submit_treeview(ans)
        db.close()

    def view_hasnot_submit(self):
        jid = self.hasset[self.row_index][0]
        cid = self.hasset[self.row_index][8]
        db = DBHelper()
        ans = db.get_job_hasnotsubmit(jid,cid)
        new_window = View_job_hasnot_submit_treeview(ans)
        db.close()
    def back(self):
        self.root2.destroy()
        self.__init__(self.hasset,self.tid)

class tea_view_hasview_job:
    def __init__(self, Hasset,tid):
        self.root = tk.Tk()
        self.tid = tid
        self.hasset = Hasset
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("作业查看情况")
        self.set_treeview()

    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root,
                                 columns=("J_id","JName", "JChapter", "JRequire", "JType", 'start_time', 'end_time','sc_id','c_id'),
                                 show="headings")
        self.tree.heading("J_id", text="作业编号")
        self.tree.heading("JName", text="作业名")
        self.tree.heading("JChapter", text="章节信息")
        self.tree.heading("JRequire", text="作业要求")
        self.tree.heading("JType", text="作业类型")
        self.tree.heading("start_time", text="开始时间")
        self.tree.heading("end_time", text="截止时间")
        self.tree.heading("sc_id", text="班级号")
        self.tree.heading("c_id", text="课程号")

        # 添加示例数据
        data = self.hasset

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        # 绑定单击事件
        self.tree.bind("<ButtonRelease-1>", self.on_tree_click)

    def on_tree_click(self, event):
        # 获取当前选中的项
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            all_items = self.tree.get_children()
            self.row_index = all_items.index(item_id)
            self.new_window(self.row_index)
    def new_window(self,id):
        job_name = self.hasset[id][1]
        self.root.destroy()
        self.root2 = tk.Tk()
        self.time = '2024-5-12'
        self.custom_font = font.Font(family="Helvetica", size=15)
        self.label_job_name = tk.Label(self.root2,text=job_name,font = self.custom_font)
        self.btn_view_has_submit = tk.Button(self.root2,text='已查看作业名单',font = self.custom_font,command = self.view_has_view)
        self.btn_view_hasnot_submit = tk.Button(self.root2,text='未查看作业名单',font = self.custom_font,command = self.view_hasnot_view)
        self.btn_back = tk.Button(self.root2, text="返回", font=self.custom_font, command=self.back)
        self.set_new_window()
        self.root2.mainloop()
    def set_new_window(self):
        #self.root2.geometry("400x500+100+100")
        self.root2.title("作业信息")
        # 创建用户名标签和文本框，使用 grid() 函数水平放置
        self.label_job_name.grid(row=0, column=0, padx=10, pady=10)
        self.btn_view_has_submit.grid(padx=20, pady=20)  # 跨两列放置，设置边距
        self.btn_view_hasnot_submit.grid(padx=20, pady=20)  # 跨两列放置，设置边距
        self.btn_back.grid(padx=20, pady=20)  # 跨两列放置，设置边距
    def view_has_view(self):
        jid = self.hasset[self.row_index][0]
        db = DBHelper()
        sid,sname,tem = db.get_stu_view_job(jid)
        new_window = View_job_has_view_treeview(sname)
        db.close()

    def view_hasnot_view(self):
        jid = self.hasset[self.row_index][0]
        db = DBHelper()
        ans = db.get_stu_notview_job(jid)
        new_window = View_job_has_notview_treeview(ans)
        db.close()
    def back(self):
        self.root2.destroy()
        self.__init__(self.hasset,self.tid)


class tea_assign_job:
    def __init__(self,cid,cname,tid):
        self.root = tk.Tk()
        self.cid = cid
        self.cname = cname
        self.tid = tid
        self.jid = self.get_jid()
        self.custom_font = font.Font(family="Helvetica", size=20)
        self.frame_id = tk.Frame(self.root)
        self.frame_name = tk.Frame(self.root)
        self.frame_require = tk.Frame(self.root)
        self.frame_type = tk.Frame(self.root)
        self.frame_chapter = tk.Frame(self.root)
        self.frame_btn = tk.Frame(self.root)
        self.frame_start = tk.Frame(self.root)
        self.frame_end = tk.Frame(self.root)
        self.frame_sc = tk.Frame(self.root)
        self.initwindow()

    def initwindow(self):
        self.root.title('编辑作业信息')
        #将label和entry加入到frame中去
        self.set_frame()
        #设置frame
        self.frame_id.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_name.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_require.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_type.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_chapter.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_start.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_end.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_sc.pack(expand=True,padx=20, pady=20, fill=tk.BOTH)
        self.frame_btn.pack(expand=True, padx=20, pady=20, fill=tk.BOTH)

        self.root.mainloop()
    def set_frame(self):
        self.set_label_Text()

    def set_label_Text(self):
        self.label_id = tk.Label(self.frame_id, text='作业编号', font=self.custom_font)
        self.label_id.pack(side=tk.LEFT)
        self.entry_id = tk.Label(self.frame_id, text=self.jid, width=50, height=1)
        self.entry_id.pack(side=tk.RIGHT)

        self.label_name = tk.Label(self.frame_name, text='作业名', font=self.custom_font)
        self.label_name.pack(side=tk.LEFT)
        self.entry_name = tk.Text(self.frame_name, width=50, height=1)
        self.entry_name.pack(side=tk.RIGHT)

        self.label_require = tk.Label(self.frame_require, text='作业要求', font=self.custom_font)
        self.label_require.pack(side=tk.LEFT)
        self.entry_require = tk.Text(self.frame_require, width=50, height=2)
        self.entry_require.pack(side=tk.RIGHT)

        self.label_type = tk.Label(self.frame_type, text='作业类型', font=self.custom_font)
        self.label_type.pack(side=tk.LEFT)
        self.entry_type = tk.Text(self.frame_type, width=50, height=1)
        self.entry_type.pack(side=tk.RIGHT)

        self.label_chapter = tk.Label(self.frame_chapter, text='章节信息', font=self.custom_font)
        self.label_chapter.pack(side=tk.LEFT)
        self.entry_chapter = tk.Text(self.frame_chapter, width=50, height=1)
        self.entry_chapter.pack(side=tk.RIGHT)

        self.label_start = tk.Label(self.frame_start, text='开始时间', font=self.custom_font)
        self.label_start.pack(side=tk.LEFT)
        self.entry_start = tk.Text(self.frame_start, width=50, height=1)
        self.entry_start.pack(side=tk.RIGHT)

        self.label_end = tk.Label(self.frame_end, text='截止时间', font=self.custom_font)
        self.label_end.pack(side=tk.LEFT)
        self.entry_end = tk.Text(self.frame_end, width=50, height=1)
        self.entry_end.pack(side=tk.RIGHT)

        self.label_sc = tk.Label(self.frame_sc, text='班级号', font=self.custom_font)
        self.label_sc.pack(side=tk.LEFT)
        self.entry_sc = tk.Text(self.frame_sc, width=50, height=1)
        self.entry_sc.pack(side=tk.RIGHT)

        self.btn_assign = tk.Button(self.frame_btn, text='布置', font=self.custom_font, command=self.assign)
        self.btn_assign.pack(side = tk.LEFT)
        self.btn_back = tk.Button(self.frame_btn, text='返回', font=self.custom_font, command=self.back)
        self.btn_back.pack(side=tk.RIGHT)


    def get_jid(self):
        db = DBHelper()
        ans = db.get_add_job_jid()
        db.close()
        return ans
    def assign(self):
        jid =self.jid
        jname = getcontent(self.entry_name.get("1.0", tk.END))
        jchapter = getcontent(self.entry_chapter.get("1.0", tk.END))
        jrequire = getcontent(self.entry_require.get("1.0", tk.END))
        jtype = getcontent(self.entry_type.get("1.0", tk.END))
        tid = self.tid
        cid = self.cid
        start = getcontent(self.entry_start.get("1.0", tk.END))
        end = getcontent(self.entry_end.get("1.0", tk.END))
        sc= getcontent(self.entry_sc.get("1.0", tk.END))

        self.new_job = Job(jid,jname,jchapter,jrequire,jtype,tid,cid,start,end,sc)
        db = DBHelper()
        db.tea_add_job(self.new_job)
        db.close()
        messagebox.showinfo('布置成功', '已布置作业！')
        self.root.destroy()

    def back(self):
        self.root.destroy()


class stu_view_tea_hasset_job:
    def __init__(self, Hasset,sid,tid):
        self.root = tk.Tk()
        self.sid = sid
        self.tid = tid
        self.hasset = Hasset
        self.initialize_gui()
        self.insert_view_job()
    def insert_view_job(self):
        db = DBHelper()
        print(self.hasset)
        jid = []
        for job in self.hasset:
            jid.append(job[0])
        for tem_jid in jid:
            if(db.do_stu_view(self.sid,tem_jid)):#如果查看了就不进行任何操作
                pass
            else:
                db.stu_view_job(self.sid,tem_jid)
        db.close()

    def initialize_gui(self):
        self.root.title("作业信息")
        self.set_treeview()

    def set_treeview(self):
        # 创建Treeview
        self.tree = ttk.Treeview(self.root,
                                 columns=("J_id","JName", "JChapter", "JRequire", "JType", 'start_time', 'end_time','sc_id','c_id'),
                                 show="headings")
        self.tree.heading("J_id", text="作业编号")
        self.tree.heading("JName", text="作业名")
        self.tree.heading("JChapter", text="章节信息")
        self.tree.heading("JRequire", text="作业要求")
        self.tree.heading("JType", text="作业类型")
        self.tree.heading("start_time", text="开始时间")
        self.tree.heading("end_time", text="截止时间")
        self.tree.heading("sc_id", text="班级号")
        self.tree.heading("c_id", text="课程号")

        # 添加示例数据
        data = self.hasset

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # 设置Treeview布局
        self.tree.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=self.tree.xview)
        scrollbar.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=scrollbar.set)

