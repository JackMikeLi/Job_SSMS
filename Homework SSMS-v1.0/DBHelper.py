import pymssql
from tool import getcontent

class DBHelper:
    stu_all_sql = "SELECT * FROM Student"
    tea_all_sql = "SELECT * FROM Teacher"
    cou_all_sql = "select * from Courses"
    sc_all_sql = "select * from Student_Class"
    teaching_all_sql = "select * from Teaching"
    takeclass_all_sql = "select * from TakeClass"
    job_all_sql = "Select * from Job "
    submit_all_sql = "Select * from Job_Submit"
    view_all_sql = "Select * from Job_View"
    def __init__(self):
        self.connect = pymssql.connect(server='192.168.1.106',
                                       user='sa',
                                       password='123456789',
                                       database='JobDB',
                                       charset='utf8',
                                       autocommit=True)
        if self.connect:
            print("数据库已经连接成功")
        self.cursor = self.connect.cursor()  # 创建一个游标对象，python里面的语句都要通过cursor来执行

    def stu_info(self):#查询学生表信息
        self.cursor.execute(self.stu_all_sql)
        id,name,sex,age,major,sc_num= [],[],[],[],[],[]
        for row in self.cursor.fetchall():
            #获取每一行中各列的内容
            col1,col2,col3,col4,col5,col6 = row
            #去掉空格
            col1, col2, col3, col4, col5, col6 = getcontent(col1),getcontent(col2),getcontent(col3),getcontent(col4),getcontent(col5),getcontent(col6)
            #加到属性列中去
            col2,col3,col5 = col2.encode('latin1').decode('gbk'),col3.encode('latin1').decode('gbk'),col5.encode('latin1').decode('gbk')
            id.append(col1),name.append(col2),sex.append(col3),age.append(col4),major.append(col5),sc_num.append(col6)
        return id,name,sex,age,major,sc_num
    def tea_info(self):#查询教师表信息
        self.cursor.execute(self.tea_all_sql)
        id,name,sex = [],[],[]
        for row in self.cursor.fetchall():
            col1,col2,col3 = row
            col1,col2,col3 = getcontent(col1),getcontent(col2),getcontent(col3)
            col2,col3 = col2.encode('latin1').decode('gbk'),col3.encode('latin1').decode('gbk')
            id.append(col1),name.append(col2),sex.append(col3)
        return id,name,sex
    def courses_info(self):#查询课程表信息
        self.cursor.execute(self.cou_all_sql)
        courses = []
        for row in self.cursor.fetchall():
            col1,col2,col3 = row
            col1,col2,col3 = getcontent(col1),getcontent(col2),getcontent(col3)
            col2 = col2.encode('latin1').decode('gbk')
            courses.append((col1,col2,col3))
        return courses
    def sc_info(self):#查询班级表信息
        self.cursor.execute(self.sc_all_sql)
        sc = []
        for row in self.cursor.fetchall():
            print(row)
            col1,col2 = row
            col1= getcontent(col1)
            sc.append((col1,col2))
        return sc
    def teaching_info(self):#查询授课表信息
        self.cursor.execute(self.teaching_all_sql)
        tid,cid = [],[]
        for row in self.cursor.fetchall():
            col1,col2 = row
            col1,col2 = getcontent(col1),getcontent(col2)
            tid.append(col1),cid.append(col2)
        return tid,cid
    def takeclass_info(self):#查询选课表信息
        self.cursor.execute(self.takeclass_all_sql)
        sid,cid = [],[]
        for row in self.cursor.fetchall():
            col1,col2 = row
            col1,col2 = getcontent(col1),getcontent(col2)
            sid.append(col1),cid.append(col2)
        return sid,cid
    def job_info(self):#查询作业表信息
        self.cursor.execute(self.job_all_sql)
        jid,jname,jchapter,jrequire,jtype,tid,cid,start,end,sc =[],[],[],[],[],[],[],[],[],[]
        for row in self.cursor.fetchall():
            col1, col2, col3, col4,col5,col6,col7,col8,col9,col10 = row
            col1, col2, col3, col4, col5, col6, col7, col10 = getcontent(col1),getcontent(col2),getcontent(col3),getcontent(col4),getcontent(col5),getcontent(col6),getcontent(col7),getcontent(col10)
            col2,col3,col4,col5 = col2.encode('latin1').decode('gbk'),col3.encode('latin1').decode('gbk'),col4.encode('latin1').decode('gbk'),col5.encode('latin1').decode('gbk')
            jid.append(col1),jname.append(col2),jchapter.append(col3),jrequire.append(col4),jtype.append(col5),tid.append(col6),cid.append(col7),start.append(col8),end.append(col9),sc.append(col10)
        return jid,jname,jchapter,jrequire,jtype,tid,cid,start,end,sc
    def Submit_info(self):#查询作业提交信息
        self.cursor.execute(self.submit_all_sql)
        sid,jid,content,time = [],[],[],[]
        for row in self.cursor.fetchall():
            col1,col2,col3,col4 = row
            col1,col2,col3 = getcontent(col1),getcontent(col2),getcontent(col3)
            col3 = col3.encode('latin1').decode('gbk')
            sid.append(col1),jid.append(col2),content.append(col3),time.append(col4)
        return sid,jid,content,time
    def View_info(self):#查询作业查看信息
        self.cursor.execute(self.view_all_sql)
        sid,jid = [],[]
        for row in self.cursor.fetchall():
            col1,col2 = row
            col1,col2 = getcontent(col1),getcontent(col2)
            sid.append(col1),jid.append(col2)
        return sid,jid
    def get_stu_class(self,sid):#查询某位学生上的所有课
        sql = "SELECT tc.C#,CName,t.T# FROM TakeClass AS tc, Courses AS c ,Teaching t WHERE tc.S# = '{}' AND tc.C# = c.C# AND tc.C# = t.C# ".format(sid)
        print(sql)
        self.cursor.execute(sql)
        cid,cname,tid = [],[],[]
        for row in self.cursor.fetchall():
            col1 ,col2 ,col3= row
            col1 ,col2 ,col3= getcontent(col1),getcontent(col2),getcontent(col3)
            col2 = col2.encode('latin1').decode('gbk')
            cid.append(col1),cname.append(col2),tid.append(col3)
        return cid,cname,tid

    def get_tea_class(self,name):#获取老师的授课课程
        sql = "SELECT t.C#,CName from Teaching t ,Teacher t2 ,Courses c where t.T# = t2.T# and c.C# = t.C# and TName = '{}'".format(name)
        print(sql)
        self.cursor.execute(sql)
        id,name= [],[]
        for row in self.cursor.fetchall():
            col1,col2= row
            col1,col2= getcontent(col1),getcontent(col2)
            col2 = col2.encode('latin1').decode('gbk')
            id.append(col1),name.append(col2)
        return id,name
    def get_stu_should_sub(self,name,time):#查询某位同学需要做的作业
        sql = "SELECT J#,JName,JChapter,JRequire,JType,start_time,end_time FROM Job as J where start_time <= '{}' AND end_time >= '{}'  AND C# in (SELECT TC.C# FROM TakeClass as TC,Student as S where TC.S# =S.S# AND S.SName = '{}')".format(time,time,name)
        print(sql)
        self.cursor.execute(sql)
        ans = []
        for row in self.cursor.fetchall():
            col1,col2,col3,col4,col5,col6,col7 = row
            col1,col2, col3, col4, col5 = getcontent(col1), getcontent(col2), getcontent(col3), getcontent(col4),getcontent(col5)
            col2,col3,col4,col5 = col2.encode('latin1').decode('gbk'),col3.encode('latin1').decode('gbk'),col4.encode('latin1').decode('gbk'),col5.encode('latin1').decode('gbk')
            ans.append((col1,col2,col3,col4,col5,col6,col7))
        return ans
    def get_tea_hasset_job(self,id,time):#获取某位老师已经布置的作业
        sql = "SELECT J#,JName,JChapter,JRequire,JType,start_time,end_time,SC#,C# FROM Job j ,Teacher t where j.T# = t.T# and t.T# = {} and start_time <='{}' AND end_time >= '{}'".format(id,time,time)
        print(sql)
        self.cursor.execute(sql)
        ans = []
        for row in self.cursor.fetchall():
            col1, col2, col3, col4, col5, col6,col7,col8,col9= row
            col1, col2, col3, col4,col5,col8,col9= getcontent(col1), getcontent(col2), getcontent(col3), getcontent(col4),getcontent(col5),getcontent(col8),getcontent(col9)
            col2, col3, col4, col5 = col2.encode('latin1').decode('gbk'), col3.encode('latin1').decode('gbk'), col4.encode('latin1').decode('gbk'), col5.encode('latin1').decode('gbk')
            ans.append((col1,col2,col3,col4,col5,col6,col7,col8,col9))
        return ans
    def get_job_hassubmit(self,jid):#获取某个作业已经提交的信息
        #查询某个作业已经提交的学生名单
        sql = "SELECT SName,J_content,J_time FROM Job_Submit js,Student s where js.J# = {} and s.S# =js.S# ".format(jid)
        print(sql)
        self.cursor.execute(sql)
        ans = []
        for row in self.cursor.fetchall():
            col1,col2,col3 = row
            col1,col2 = getcontent(col1),getcontent(col2)
            col1,col2 = col1.encode('latin1').decode('gbk'),col2.encode('latin1').decode('gbk')
            ans.append((col1,col2,col3))
        return ans
    def get_job_hasnotsubmit(self,jid,cid):#获取某个作业未提交的名单
        sql = "SELECT SName FROM TakeClass tc,Student s where tc.S# = s.S# and TC.C# = {} and tc.S# not in (SELECT S# FROM Job_Submit js WHERE js.J# = {})".format(cid,jid)
        print(sql)
        self.cursor.execute(sql)
        ans = []
        for row in self.cursor.fetchall():
            col1 = row[0]
            col1 = getcontent(col1)
            col1 = col1.encode('latin1').decode('gbk')
            ans.append(col1)
        return ans
    def stu_submit_job(self,sid,jid,content,time):#某个学生提交作业
        content = getcontent(content)
        values = "{},{},'{}','{}'".format(sid,jid,content,time)
        print(values)
        sql = "insert into Job_Submit (S#,J#,J_content,J_time) values ({})".format(values)
        print(sql)
        self.cursor.execute(sql)
    def stu_update_job(self,sid,jid,content,time):#某个学生更新作业
        content = getcontent(content)
        values = "{},{},'{}','{}'".format(sid, jid, content, time)
        print(values)
        sql = "UPDATE Job_Submit SET J_content = '{}',J_time = '{}' WHERE S# = {} and J# = {}".format(content,time,sid,jid)
        print(sql)
        self.cursor.execute(sql)
    def do_stu_submit(self,sid,jid):#判断某位学生是否提交了某份作业
        #用来判断学生是否提交这个作业
        sql = "select * FROM Job_Submit js where S# = {} and J# ={}".format(sid,jid)
        print(sql)
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        if row == []:
            return False
        else:
            return True
    def tea_add_job(self,job):#教师布置作业
        values = "({},'{}','{}','{}','{}',{},{},'{}','{}',{})".format(job.id,job.name,job.jchapter,job.jrequire,job.jtype,job.tid,job.cid,job.start,job.end,job.sc)
        print(values)
        sql = "insert into Job (J#,JName,JChapter,JRequire,JType,T#,C#,start_time,end_time,SC#) values " + values
        print(sql)
        self.cursor.execute(sql)


    def get_add_job_jid(self):#获取新添加的作业编号（递增）
        ans = self.job_info()
        num = max([int(num) for num in ans[0]]) + 1
        print(num)
        return num
    def get_stu_view_job(self,jid):#查询某个作业中已查看作业学生名单
        sql = "SELECT * FROM ViewJob jv where jv.J# = {}".format(jid)
        print(sql)
        self.cursor.execute(sql)
        sid,sname,jid = [],[],[]
        for row in self.cursor.fetchall():
            col1,col2,col3 = row
            col1,col2,col3 = getcontent(col1),getcontent(col2),getcontent(col3)
            col2 = col2.encode('latin1').decode('gbk')
            sid.append(col1),sname.append(col2),jid.append(col3)
        return sid,sname,jid
    def get_stu_notview_job(self,jid):#查询某个作业未查看的学生名单
        sql = "SELECT SName FROM JobShouldSubmit jss WHERE jss.J# = {} AND SName not in(SELECT SName FROM ViewJob jv where jv.J# = {})".format(jid,jid)
        print(sql)
        self.cursor.execute(sql)
        ans = []
        for row in self.cursor.fetchall():
            col1 = row[0]
            col1 = getcontent(col1)
            col1 = col1.encode('latin1').decode('gbk')
            ans.append(col1)
        return ans
    def do_stu_view(self,sid,jid):#判断某位学生是否查看了某份作业信息
        sql = "SELECT * FROM Job_View jv WHERE S# ={} AND J# ={}".format(sid,jid)
        print(sql)
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        if row == []:#查看了返回True,未查看返回False
            return False
        else:
            return True
    def stu_view_job(self,sid,jid):#某个学生查看作业，进行数据插入
        values = "({},{})".format(sid,jid)
        print(values)
        sql = "insert into Job_View (S#,J#) values " + values
        print(sql)
        self.cursor.execute(sql)
    def do_stu_oneday_job(self,sid):#查询某个学生是否还有一天截止的作业
        sql = "SELECT J#,JName FROM Job j JOIN TakeClass tc ON j.C# = tc.C# where tc.S# = {} AND J# in(SELECT J# FROM JobInOneDay jiod)".format(sid)
        print(sql)
        self.cursor.execute(sql)
        ans = []
        for row in self.cursor.fetchall():
            col1,col2 = row
            col1,col2 = getcontent(col1),getcontent(col2)
            col2 = col2.encode('latin1').decode('gbk')
            ans.append((col1,col2))
        return ans

    def __del__(self):
        self.close()

    def close(self):
        if self.connect:
            self.connect.commit()  # 提交
            self.cursor.close()
            self.connect.close()
            self.connect = None
