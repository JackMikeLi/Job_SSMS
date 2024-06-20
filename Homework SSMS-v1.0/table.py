class Student:
    def __init__(self, id=None, name=None, sex=None, age=None, major=None, sc_id=None):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age
        self._major = major
        self._sc_id = sc_id

    # id property
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # sex property
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    # age property
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    # major property
    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    # sc_num property
    @property
    def sc_num(self):
        return self._sc_id

    @sc_num.setter
    def sc_num(self, value):
        self._sc_id = value
    def show_info(self):
        print(self.id,self.name,self.sex,self.age,self.major,self.sc_num)
class Teacher:

    def __init__(self,id=None,name=None,sex=None):
        self.id = id
        self.name = name
        self.sex = sex

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # sex property
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    def show_info(self):
        print(self.id,self.name,self.sex)
class Courses:
    def __init__(self,id,name,sc_id):
        self.id = id
        self.name = name
        self.sc_id = sc_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sc_num(self):
        return self._sc_id

    @sc_num.setter
    def sc_num(self, value):
        self._sc_id = value
class Teaching:
    def __init__(self, t_id, c_id):
        self._t_id = t_id
        self._c_id = c_id

    # t_id property
    @property
    def t_id(self):
        return self._t_id

    @t_id.setter
    def t_id(self, value):
        self._t_id = value

    # c_id property
    @property
    def c_id(self):
        return self._c_id

    @c_id.setter
    def c_id(self, value):
        self._c_id = value
class TakeClass:
    def __init__(self, s_id, c_id):
        self._s_id = s_id
        self._c_id = c_id

    # s_id property
    @property
    def s_id(self):
        return self._s_id

    @s_id.setter
    def s_id(self, value):
        self._s_id = value

    # c_id property
    @property
    def c_id(self):
        return self._c_id

    @c_id.setter
    def c_id(self, value):
        self._c_id = value
class Student_Class:
    def __init__(self, sc_id, sc_num):
        self._sc_id = sc_id
        self._sc_num = sc_num

    # sc_id property
    @property
    def sc_id(self):
        return self._sc_id

    @sc_id.setter
    def sc_id(self, value):
        self._sc_id = value

    # sc_num property
    @property
    def sc_num(self):
        return self._sc_num

    @sc_num.setter
    def sc_num(self, value):
        self._sc_num = value

class Job:
    def __init__(self, id, name, jchapter, jrequire, jtype, tid, cid, start, end, sc):
        self._id = id
        self._name = name
        self._jchapter = jchapter
        self._jrequire = jrequire
        self._jtype = jtype
        self._tid = tid
        self._cid = cid
        self._start = start
        self._end = end
        self._sc = sc

    # id property
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # jchapter property
    @property
    def jchapter(self):
        return self._jchapter

    @jchapter.setter
    def jchapter(self, value):
        self._jchapter = value

    # jrequire property
    @property
    def jrequire(self):
        return self._jrequire

    @jrequire.setter
    def jrequire(self, value):
        self._jrequire = value

    # jtype property
    @property
    def jtype(self):
        return self._jtype

    @jtype.setter
    def jtype(self, value):
        self._jtype = value

    # tid property
    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, value):
        self._tid = value

    # cid property
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value

    # start property
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    # end property
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    # sc property
    @property
    def sc(self):
        return self._sc

    @sc.setter
    def sc(self, value):
        self._sc = value

