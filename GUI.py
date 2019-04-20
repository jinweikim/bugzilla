import tkinter as tk
import tools
window = tk.Tk()
window.title('面向软件缺陷的自动问答系统')
window.geometry('300x300')
e = tk.Entry(window,show=None)
e.pack()
def getTemplate():
    n = tools.sen2NLPatt(e.get())
    var = tools.getTemplate_1(n)
    t.delete(0.0,tk.END)
    t.insert('insert',var)

b1 = tk.Button(window,text='生成模板',width=15,height=2,command=getTemplate)
b1.pack()

t=tk.Text(window,height=2)
t.pack()
window.mainloop()