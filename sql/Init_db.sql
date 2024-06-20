IF NOT EXISTS (
    SELECT name 
    FROM sys.databases 
    WHERE name = 'JobDB'
)
BEGIN
    CREATE DATABASE JobDB;
END;

use JobDB

--创建表

create table Teacher(--教师表
	T# char(8) not null,
	TName char(10) not null,
	Sex char(4) not null,
	primary key(T#)
)

create table Student_Class(--班级表
	SC# char(8) not null,
	SC_count int not null,
	primary key(SC#)
)

create table Courses(--课程表
	C# char(8) not null,
	CName char(10) not null,
	SC# char(8) not null,
	primary key(C#),
	foreign key(SC#) references Student_Class(SC#),
)

create table Student(--学生表
	S# char(8) not null,
	SName char(10) not null,
	sex char(4) not null,
	age char(4) not null,
	major char(30) not null,
	SC# char(8) not null,
	primary key(S#),
	foreign key(SC#) references student_class(SC#),
)

create table Teaching(--授课表
	T# char(8) not null,
	C# char(8) not null,
	primary key(T#,C#),
	foreign key(T#) references Teacher(T#),
	foreign key(C#) references Courses(C#)
)

create table TakeClass(--选课表
	S# char(8) not null,
	C# char(8) not null,
	primary key(S#,C#),
	foreign key(S#) references Student(S#),
	foreign key(C#) references Courses(C#)
)

create table Job(--作业表
	J# char(8) not null,
	JName char(50) not null,
	JChapter char(50) not null,--所属章节信息
	JRequire char(50) not null,--作业要求
	JType char(50) not null,--作业类型
	T# char(8) not null,
	C# char(8) not null,
	start_time datetime not null,
	end_time datetime not null,
	SC# char(8) not null,
	primary key(J#),
	foreign key(C#) references Courses(C#),
	foreign key(T#) references Teacher(T#),
	foreign key(SC#) references Student_Class(SC#)
)

create table Job_View(--作业查看表
	S# char(8) not null,
	J# char(8) not null,
	primary key(S#,J#),
	foreign key(S#) references Student(S#),
	foreign key(J#) references Job(J#)
)

create table Job_Submit(--作业提交表
	S# char(8) not null,
	J# char(8) not null,
	J_content char(50) not null,
	J_time datetime not null,
	primary key(S#,J#),
	foreign key(S#) references Student(S#),
	foreign key(J#) references Job(J#)
)



--插入数据

insert into Teacher--插入教师表
(T#,TName,Sex)
values
(1101,'格言','女'),(1102,'刘金子','女'),(1103,'王招财','男'),(1104,'刘态杠','男'),
(1105,'鲁鹏','男'),(1106,'包晓光','男'),(1107,'王晓明','女'),(1108,'肖齐话','女')

insert into Student_Class--插入班级表
(SC#,SC_count)
values
(501,6),(502,6)

insert into Courses--插入课程表
(C#,CName,SC#)
values
(101,'数据库原理',501),(102,'复变函数',501),
(103,'运筹学',501),(104,'数学建模',501),
(105,'数据科学',502),(106,'数据库原理',502),
(107,'计算机网络',502),(108,'操作系统',502)

insert into Student--插入学生表表
(S#,SName,sex,age,major,SC#)
values
(2101,'孙悟空','男',20,'计算机科学',501),(2102,'八戒','男',22,'计算机科学',501),
(2103,'沙悟净','男',24,'计算机科学',501),(2104,'唐僧','男',19,'计算机科学',501),
(2105,'牛小花','女',18,'计算机科学',501),(2106,'张欣然','女',20,'计算机科学',501),
(2201,'关羽','男',20,'数据科学',502),(2202,'刘备','男',21,'数据科学',502),
(2203,'小乔','女',20,'数据科学',502),(2204,'大乔','女',21,'数据科学',502),
(2205,'吕布','男',19,'数据科学',502),(2206,'曹操','男',20,'数据科学',502)


insert into Teaching--插入授课表
(T#,C#)
values
(1101,101),(1102,102),(1103,103),(1104,104),
(1105,105),(1106,106),(1107,107),(1108,108)

insert into TakeClass--插入选课表
(S#,C#)
values
(2101,101),(2101,102),(2101,103),(2101,104),
(2102,101),(2102,102),(2102,103),
(2103,101),(2103,102),(2103,103),(2103,104),
(2104,101),(2104,102),(2104,103),
(2105,101),(2105,102),(2105,103),(2105,104),
(2106,101),(2106,102),(2106,103),
(2201,105),(2201,106),(2201,107),(2201,108),
(2202,105),(2202,106),(2202,107),
(2203,105),(2203,106),(2203,107),(2203,108),
(2204,105),(2204,106),(2204,107),
(2205,105),(2205,106),(2205,107),(2205,108),
(2206,105),(2206,106),(2206,107)

insert into Job --插入作业表
(J#,JName,JChapter,JRequire,JType,T#,C#,start_time,end_time,SC#)
values
(1,'数据库第一次作业','第一章','数据库原理实验报告一初识数据库','实验报告',1101,101,'2024-05-8 12:00:00','2024-05-13 12:00:00',501),
(2,'数据库第二次作业','第二章','数据库原理实验报告-多表查询','实验报告',1101,101,'2024-05-8 12:00:00','2024-05-14 12:00:00',501),
(3,'运筹学第二次作业','第一章','用单纯形法求线性规划问题','纸质手写',1103,103,'2024-05-8 12:00:00','2024-05-20 12:00:00',501),
(4,'数据科学第二次作业','第三章','对数据进行描述性统计','实验报告',1105,105,'2024-05-8 12:00:00','2024-05-28 12:00:00',502),
(5,'计算机网络第三次作业','绪论','对计算机网络进行简单介绍','ppt',1107,107,'2024-05-15 12:00:00','2024-05-31 12:00:00',502)

insert into Job_View --插入作业查看表
(J#,S#)
values
(1,2101),(1,2102),(1,2103),(1,2104),
(2,2101),(2,2103),(2,2104),
(3,2102),(3,2103),(3,2204),
(4,2203),(4,2204)

insert into Job_Submit --插入作业提交表
(J#,S#,J_content,J_time)
values
(1,2101,'初始数据库，我们安装了SSMS、SQL SERVER','2024-5-9'),
(2,2102,'数据库好难，学不会','2024-05-9'),
(3,2103,'单纯刑法','2024-05-10'),
(4,2201,'数据不科学','2024-05-12')


--创建视图
	
--创建一个视图来统计当前活动状态作业提交的学生名单
CREATE VIEW JobSubmit AS
SELECT J.JName,start_time,end_time,S.SName
FROM Job_Submit as JS,Student as S,Job as J
WHERE S.S# = JS.S# AND J.J# = JS.J# AND start_time <= '2024-5-12' AND end_time >= '2024-5-12'

--创建一个视图来统计每份作业应该提交作业的同学
CREATE VIEW JobShouldSubmit AS
SELECT J.J#,J.JName,start_time,end_time,S.SName FROM Job j ,Student_Class sc ,Student s 
WHERE J.SC# = SC.SC# AND s.SC# =sc.SC#


--创建一个视图统计目前未提交作业的所有同学
CREATE VIEW JobNotSubmit AS
Select * FROM JobShouldSubmit JSS
EXCEPT
SELECT * From JobSubmit

--创建视图，统计还有1天截止的作业
CREATE VIEW JobInOneDay AS
SELECT J#,JName,start_time,end_time FROM Job j
WHERE DATEDIFF(day, '2024-5-12' , end_time) = 1

--创建视图统计作业查看情况
CREATE VIEW ViewJob AS
SELECT s.S#,SName,J# FROM Student s 
RIGHT Join Job_View jv ON jv.S# = s.S# 



