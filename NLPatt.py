class NLPatt:

    types = []#储存实体类型
    supp = []#储存实体对
    str = ''
    counter = 0

    def __init__(self,str,types,supp):
        self.str = str
        self.types = types
        self.supp = supp

    def __str__(self):
        return self.str

