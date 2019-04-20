import rdflib
import nltk
from NLPatt import NLPatt

Product_list = []
Bug_name_list = []
Reported_time = []
Modified_time = []
Component_list = []
Assignee_list = []
Reporter_list = []
TriageOwner_list = []
Description_list = []


g = rdflib.Graph()

#判断字符串是否是Bug_id,条件有二,字符全为数字且长度大于3
def isBugid(str):
    if str.isdigit():
        if len(str) < 3:
            return False
        return True
    else:
        return False

#判断字符串是否是Product
def isProduct(str):
    list=[]
    file2list('product_list',list)
    for l in list:
        if(str == l.strip().strip("'")):
            return True
    return False

#判断字符串是够是Component
def isComponent(str):
    list = []
    file2list('Component_list', list)
    for l in list:
        if (str == l.strip().strip("'")):
            return True
    return False

#求语句的支持对(也就是实体对)
def supp(str):
    supp_piar = []
    tokens = nltk.word_tokenize(str)
    for t in tokens:
        if isEntity(t):
            supp_piar.append(t)
    return supp_piar

def isEntity(str):
    if isBugid(str) | isProduct(str):
        return True
    else:
        return False

#将语句转化为自然语言模式
def sen2NLPatt(str):
    tokens = nltk.word_tokenize(str)
    newstr = str
    types = []
    supp = []
    for t in tokens:
        if isBugid(t):
            newstr = newstr.replace(t, 'Bug_id')
            types.append('Bug_id')
            supp.append(t)
        # if isProduct(t):
        #     newstr = newstr.replace(t, 'Product')
        #     supp.append(t)
        # if isComponent(t):
        #     newstr = newstr.replace(t,'Component')
        #     supp.append(t)

    #更换Bug_name
    if 'name' in newstr:
        Bug_name_list = []
        file2list('Bug_name_list', Bug_name_list)
        for r in Bug_name_list:
            if r.strip().strip("'") in newstr:
                # print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r), 'Bug_name')
                types.append('Bug_name')
                supp.append(raw(r))

    #更换Product
    if 'product' in newstr:
        prodcut_list = []
        file2list('product_list', prodcut_list)
        for r in prodcut_list:
            if r.strip().strip("'") in newstr:
                # print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r), 'Product')
                types.append('Product')
                supp.append(raw(r))

    #更换Component
    if 'component' in newstr:
        component_list = []
        file2list('Component_list', component_list)
        for r in component_list:
            if r.strip().strip("'") in newstr:
                # print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r), 'Component')
                types.append('Component')
                supp.append(raw(r))

    #更换reported时间
    if 'reported' in newstr:
        reported_list = []
        file2list('Reported_time',reported_list)
        for r in reported_list:
            if r.strip().strip("'") in newstr:
                #print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r),'Reported')
                types.append('Reported')
                supp.append(raw(r))

    #更换modified时间
    if 'modified' in newstr:
        modified_list = []
        file2list('Modified_time',modified_list)
        for r in modified_list:
            if r.strip().strip("'") in newstr:
                #print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r),'Modified')
                types.append('Modified')
                supp.append(raw(r))

    #更换assignee
    if 'assignee' in newstr:
        Assignee_list = []
        file2list('Assignee_list',Assignee_list)
        for r in Assignee_list:
            if r.strip().strip("'") in newstr:
                #print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r),'Assignee')
                types.append('Assignee')
                supp.append(raw(r))

    #更换reporter
    if 'reporter' in newstr:
        Reporter_list = []
        file2list('Reporter_list',Reporter_list)
        for r in Reporter_list:
            if r.strip().strip("'") in newstr:
                #print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r),'Reporter')
                types.append('Reporter')
                supp.append(raw(r))

    #更换Triage Owner
    if 'Triage Owner' in newstr:
        TriageOwner_list = []
        file2list('TriageOwner_list',TriageOwner_list)
        for r in TriageOwner_list:
            if r.strip().strip("'") in newstr:
                #print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r),'Triage Owner')
                types.append('TriageOwner')
                supp.append(raw(r))

    #更换description
    if 'description' in newstr:
        Description_list = []
        file2list('Description_list',Description_list)
        for r in Description_list:
            if r.strip().strip("'") in newstr:
                print(r.strip().strip("'"))
                newstr = newstr.replace(raw(r),'Description')
                types.append('Description')
                supp.append(raw(r))

    n = NLPatt(newstr,types,supp)
    return n


def getR(n):
    r = ''
    if(n.types[0] == 'Bug_id'):
        if n.types[1] == 'Bug_name':
            r = 'isBugname'
        if n.types[1] == 'Product':
            r = 'isProduct'
        if n.types[1] == 'Component':
            r = 'isComponent'
        if n.types[1] == 'Reported':
            r = 'ReportedTime'
        if n.types[1] == 'Modified':
            r = 'ModifiedTime'
        if n.types[1] == 'Assignee':
            r = 'isAssignee'
        if n.types[1] == 'Reporter':
            r = 'isReporter'
        if n.types[1] == 'TriageOwner':
            r = 'isTriageOwner'
        if n.types[1] == 'Description':
            r = 'isDescription'
    return r

#问题目标实体是bug的其他属性
def getTemplate_1(n):
    relation_dict = {'isBugname':'the bug name',
                     'isProduct':'the product',
                    'isComponent':'the component',
                    'ReportedTime':'the reported time',
                    'ModifiedTime':'the modified time',
                     'isAssignee':'the assignee',
                     'isReporter':'the reporter',
                     'isTriageOwner':'the Triage Owner',
                     'isDescription':'the Description'}
    template = []
    wh = ''
    if n.types[1] == 'Reported':
        wh = 'When is '
    elif n.types[1] == 'Modified':
        wh = 'When is '
    elif n.types[1] == 'Assignee':
        wh = 'Who is '
    elif n.types[1] == 'Reporter':
        wh = 'Who is '
    elif n.types[1] == 'TriageOwner':
        wh = 'Who is'
    else:
        wh = 'What is '

    mid = relation_dict[getR(n)] + ' of '

    last = 'the bug ' + n.supp[0] + '<' + n.types[0] + '>'

    template[0] = wh + mid + last
    template[1] = 'SELECT ?'+n.types[0]+' WHERE \n'+'{ ' +n.supp[1] +',type'+','+n.types[1]+'. ?'+n.supp[0] +',type'+','+n.types[0]+'. '+n.supp

    return template

#问题目标实体是bugid
def getTemplate_0(n):
    wh = 'which bug '
    relation_dict = {'isBugname': 'has the name',
                     'isProduct': 'has the product',
                     'isComponent': 'has the component',
                     'ReportedTime': 'was reported at',
                     'ModifiedTime': 'was modified at',
                     'isAssignee': 'has the assignee',
                     'isReporter': 'has been reported by',
                     'isTriageOwner': 'has the Triage Owner',
                     'isDescription': 'has the Description'}
    mid = relation_dict[getR(n)]
    last = ' ' + n.supp[1]
    template = wh + mid + last + '<' + n.types[1] + '>'
    return template

'''   
Daily Report:
4.13工作情况:初步完成实体识别与supp集构建的任务，但Triage Owner与Description的识别还有bug,
            Triage Ow ner由有memory error,Description_list中似乎由空数据(可以在读取文件时不读空数据,明天可以尝试一下)
4.14计划任务有:1.解决实体识别剩余的Bug
             2.进行关系确定的工作
'''

'''
4.14工作情况:尚未解决昨日两个Bug，其中Description问题出现在源数据未能完整爬取,先暂且搁置
            翻译完关系确定部分的论文，理解大体思路
4.15计划任务:准备进行关系确定            
'''


#去除字符串两端空格与单引号
def raw(str):
    return str.strip().strip("'")

#将指定的实体替换为其类型,将str中的old字符串替换为new字符串
# def replace2Types(str,old,new):
#     str = str.replace()

#把文件中的列表转化为列表,结果保存在list中
def file2list(filename,list):
    with open(filename,'r') as f:
        str = f.read()
        str = str.strip('[')
        str = str.strip(']')
        for s in str.split(','):
            list.append(s)

#plist = []
# file2list('product_list',plist)
# print(plist[0])
# print(isProduct('DevTools'))
# print(isProduct('Firefox'))
# print(isEntity('DevTools'))
# print(isEntity('Firefox'))
# print(isEntity('1306942'))
# print(isEntity('ddd'))
# print(isComponent('Activity Streams: Newta去除b'))
# print(isComponent('Inspector'))
# print(isComponent('Activity Streams: Newtab'))
# print(isComponent('Activity Streams: Newta'))
# print(isComponent('Inspetor'))

