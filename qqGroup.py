import pandas as pd
import tkinter as tk
from Crawer import craw

str1='''
--------------------------------------------
    欢迎来到由(^v^)制作的qq群成员的小程序
    请根据以下注意事项爬取进行爬取：
    1、本程序暂时只支持火狐浏览器
    2、登录后请将成员表下拉到底后关闭浏览器。
    3、本程序仅供学习。
--------------------------------------------
'''



windows =tk.Tk()
windows.resizable(False, False)
CurrentShow = tk.StringVar()
CurrentShow.set(str1)
#窗口设置
windows.title("爬取qq群成员")
windows.geometry("300x300")


def getList(number,filename):
    #获取输入框中的值
    n=number.get()
    f=str(filename.get())
    if n=="" or f=="":
        return
    #爬取网页
    menber_list=craw(n)
    if menber_list:
        data=pd.DataFrame(menber_list).T
        data.to_excel('result/'+f+'.xls')
        CurrentShow.set("爬取成功")
    else:
        CurrentShow.set("爬取失败")


def start():
    #页面布局
    qqNumber=tk.Entry(windows)
    qqNumber.place(x=50,y=50,width=200,height=30)
    qqNumber_label=tk.Label(windows,text="请输入qq群号：")
    qqNumber_label.place(x=75,y=20,width=150,height=20)
    fileName_label=tk.Label(windows,text="请输入保存的文件名：")
    fileName_label.place(x=75,y=85,width=150,height=20)
    fileName=tk.Entry(windows)
    fileName.place(x=50,y=105,width=200,height=30)
    begin=tk.Button(text="开始爬取",command=lambda :getList(qqNumber,fileName))
    begin.place(x=50,y=150,width=80,height=40)
    myQuit=tk.Button(text="退出",command=quit)
    myQuit.place(x=170,y=150,width=80,height=40)
    craw_message=tk.Label(windows,textvariable=CurrentShow,bg='white',justify='left')
    craw_message.place(x=10,y=200,width=280,height=90)

    windows.mainloop()

if __name__=="__main__":
    start()