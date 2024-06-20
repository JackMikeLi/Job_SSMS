def getcontent(s):#用于过滤数据库中的空格
    # 使用 split() 方法分割字符串，并过滤掉空字符串
    parts = s.split()
    # 返回过滤后的非空部分组成的列表
    result = ' '.join(parts)
    # 返回连接后的字符串
    return result