import nltk
import tools
s0 = 'The product of bug 1306942 is DevTools'
s1 = 'The name of bug 1306942 is Fix all-tabs-menu position in RTL locales'
s2 = 'The reported time of bug 1306942 is 3 years ago '
s3 = 'The modified time of bug 1306942 is 10 months ago'
s4 = 'The component of bug 1306942 is Inspector '
s5 = 'The assignee of bug 1306942 is [:Towkir] Ahmed '
s6 = 'The reporter of bug 1306942 is magicp'
s7 = 'The Triage Owner of bug 1306942 is Gabriel[:gl](ΦωΦ) '
s8 = '''The description of bug 1306942 is User Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0 
Build ID: 20161001030430

Steps to reproduce:

1. Start Nightly in RTL locales
2. Open DevTools > Inspector
3. Resize inspector sidebar until displaying all-tabs-menu                  


Actual results:

all-tabs-menu position is the start side.

Regression range:
https://hg.mozilla.org/integration/fx-team/pushloghtml?fromchange=52cfd2babd94fa8452128940b50614cc12660785&tochange=45513d6773f099db66f0cd7bf1e312f6f9d11475


Expected results:

all-tabs-menu should place in the end side.'''
# nltk.download()
all_s = {s0,s1,s2,s3,s4,s5,s6}
sentence = 'The product of bug 59908 is mozilla.org.Graveyard'
for s in all_s:
    n = tools.sen2NLPatt(s)
    print('原句: '+s)
    print('自然语言模式: ',end="")
    print(n)
    print('类型对: ', end="")
    print(n.types)
    print('实体对: ', end="")
    print(n.supp)
    print('关系: ', end="")
    print(tools.getR(n))
    print('模板1: ',end="")
    print(tools.getTemplate_1(n))
    print('模板0: ', end="")
    print(tools.getTemplate_0(n))
    print('\n')
# print(tools.sen2NLPatt(s7))
#print(tools.sen2NLPatt(s8))
# tokens = nltk.word_tokenize(s0)
# n0 = tools.sen2NLPatt(s0)
# n4 = tools.sen2NLPatt(s4)
# n2 = tools.sen2NLPatt(s2)
# n3 = tools.sen2NLPatt(s3)

# print(n0)
# print(n0.supp)
#
# print(n2)
# print(n2.supp)
#
# print(n3)
# print(n3.supp)
#
# print(n4)
# print(n4.supp)
#print(sentence.replace('59908','Bug_id'))
#4.13的工作安排:完成识别Component,Reporter等的方法