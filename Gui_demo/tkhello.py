"tkhello.py" #这个例子实现tkinter 的基础调用。标签，按钮和进度条组件演示
'''
要创建并运行您的GUI 程序，下面五步是基本的：
1. 导入tkinter 模块（import tkinter，或者，from tkinter import *)。
2. 创建一个顶层窗口对象，来容纳您的整个GUI 程序。
3. 在您的顶层窗口对象上（或者说在“其中”）创建所有的GUI 模块（以及功能）。
4. 把这些GUI 模块与底层程序代码相连接。
5. 进入主事件循环。
'''
import tkinter #导入tkinter 模块
from tkinter import X
from tkinter import Y
from tkinter import Tk

top=Tk() #创建一个顶层窗口对象

def resize(ev=None): #定义一个回调函数控制字符大小
    fontsize=scale.get()#根据经度条获取字符大小
    fontsize="{0} {1}{2} {3}".format('Helvetica','-',str(fontsize),'bold')
    print(fontsize)
    lab.config(font=fontsize)

'''frame1=tkinter.Frame(top) #定义组件框架，相当于C#中的panel
frame2=tkinter.Frame(top)
frame3=tkinter.Frame(top)
frame1.pack(fill=tkinter.Y, expand=1)
frame2.pack(fill=tkinter.X, expand=1)
frame3.pack(fill=tkinter.X, expand=1)
'''
lab=tkinter.Label(top,text='hello world',font='Helvetica -12 bold') #在顶层窗口对象top上创建GUI 模块
quit = tkinter.Button(top, text='QUIT',command=top.quit, bg='red', fg='white')
scale = tkinter.Scale(top, from_=10, to=40,orient=tkinter.HORIZONTAL, command=resize)
scale.set(12)
lab.pack(fill=Y, expand=1) #加载并显示lab标签
scale.pack(fill=X, expand=1)
quit.pack(fill=X, expand=1)
top.mainloop() #进入主事件循环


