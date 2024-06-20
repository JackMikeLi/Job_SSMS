# python连接SQL server数据库，输出有中文乱码

好容易把数据库连接上了，结果发现查询时候输出的中文乱码了，如下图：

![image-20240617095355842](C:\Users\Li\AppData\Roaming\Typora\typora-user-images\image-20240617095355842.png)

发现只要把在连接数据库的地方“charset = utf8”改成“charset = GBK ”就可以顺利输出中文啦

![image-20240617095413685](C:\Users\Li\AppData\Roaming\Typora\typora-user-images\image-20240617095413685.png)

修改后：

![image-20240617095439554](C:\Users\Li\AppData\Roaming\Typora\typora-user-images\image-20240617095439554.png)

![image-20240617095511916](C:\Users\Li\AppData\Roaming\Typora\typora-user-images\image-20240617095511916.png)