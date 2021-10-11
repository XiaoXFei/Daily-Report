import tkinter as tk

from tkinter import *
import tkinter.messagebox
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class GUI(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('每日一报自动填写小程序')
        # self.root.update_idletasks()
        # x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        # y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        # self.root.geometry("+%d+%d" % (x, y))

        self.root.geometry('500x300+530+250')
        # 禁止窗口拉伸
        self.root.wm_resizable(False, False)

        # label = tk.Label(root, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
        # label.pack()
        #
        # btn1 = tk.Button(root, text='hit me', font=('Arial', 12), width=10, height=1)
        # btn1.pack()
        self.var1 = StringVar()
        self.var2 = StringVar()

        self.label_account = tk.Label(self.root, text='账号', font=('Arial', 12))
        self.label_password = tk.Label(self.root, text='密码', font=('Arial', 12))

        self.input_account = tk.Entry(self.root, width=30, textvariable=self.var1)
        self.input_password = tk.Entry(self.root, show='*', width=30, textvariable=self.var2)

        self.login_btn = tk.Button(self.root, text='一键填写日报', font=('Arial', 10), command=self.login)
        self.quit_btn = tk.Button(self.root, text='退出', font=('Arial', 10), command=self.quit)

        self.Label1 = tk.Label(self.root, text='仅供内部人员使用，请勿外传！', font=('Arial', 20))
        self.Label1.pack()
        self.label_account.place(x=90, y=80)
        self.input_account.place(x=150, y=80)
        self.label_password.place(x=90, y=120)
        self.input_password.place(x=150, y=120)
        self.login_btn.place(x=160, y=170)
        self.quit_btn.place(x=280, y=170)
        self.Label2 = tk.Label(self.root, text='本小程序仅为个人方便制作，不会收集个人隐私信息！作者：ldf 版本号：v1.0', font=('Arial', 10))
        self.Label2.pack()
        self.Label3 = tk.Label(self.root, text='本程序使用google chrome插件运行，请确保本机已安装google chrome浏览器！', font=('Arial', 10))
        self.Label3.place(x=10,y=240)
        self.Label4 = tk.Label(self.root, text='点击一键填写后请勿操作，等待程序自动运行结束即可', font=('Arial', 13))
        self.Label4.place(x=30,y=260)

        self.root.mainloop()

    def login(self):
        ac = self.var1.get()
        pw = self.var2.get()
        self.Run(ac,pw)

    def quit(self):
        self.quit = tk.messagebox.askokcancel('提示', '是否退出程序？')
        if (self.quit):
            self.root.destroy()

    def getString(self):
        account = self.input_account.get().ljust(11, "")
        return account

    def Run(self,username,password):
        self.flag = 1
        try:
            print("正在加载用户信息......")

            print("正在打开浏览器........")
            self.b = webdriver.Chrome()
            self.b.get('https://hsm.sspu.edu.cn')
            print("正在登录.............")
            time.sleep(1)
            # 填写账号密码
            self.b.find_element_by_id("username").send_keys(username)
            time.sleep(1)
            self.b.find_element_by_id("password").send_keys(password)
            time.sleep(1)
            # 点击登录
            self.b.find_element_by_class_name("submit_button").click()
            time.sleep(3)
            print("正在填写每日一报......")
            # 点击“每日一报”
            self.b.find_element_by_class_name("icos").click()
            time.sleep(1)
            # 点击“良好”
            self.b.find_element_by_id("fineui_2-inputEl-icon").click()
            time.sleep(1)

            # 输入体温
            print("正在输入体温......")
            self.temp_text = self.b.find_element_by_id("p1_TiWen")
            self.temp_text.click()
            time.sleep(3)

            self.temp_input = self.b.find_element_by_id("p1_TiWen-inputEl")
            self.temp_input.send_keys(Keys.CONTROL + 'a')
            self.temp_input.send_keys(Keys.DELETE)
            time.sleep(2)

            self.b.find_element_by_id("fineui_37").click()
            time.sleep(1)
            self.temp_input.send_keys("36")
            # b.find_element_by_class_name("f-field-body-cell-centerpart").send_keys("37")

            time.sleep(2)
            # f-tool-icon f-icon f-iconfont f-iconfont-close

            # 点击“点击提交”
            print("提交中...............")
            self.b.find_element_by_id("p1_ctl00_btnSubmit").click()

            time.sleep(3)
            # 点击“完成”
            self.b.find_element_by_id("fineui_39").click()
            time.sleep(1)
            print("每日一报自动提交完成！")
            print("程序自动关闭中........")
            time.sleep(1)
            # 关闭页面
            self.b.quit()
        except:
            self.flag = 0
            self.b.quit()
        self.check(self.flag)

    def check(self,f):
        print(f)
        if(f==0):
            self.warning()
        elif(f==1):
            self.confirm()

    def warning(self):
        err = tk.messagebox.askretrycancel('出错了！', '每日一报填写出错啦！请确保已安装Google Chrome浏览器并检查账号密码是否输入正确！若无问题请与管理员取得联系！')
        # print(err)

    def confirm(self):
        ok = tk.messagebox.showwarning('自动填写成功！','每日一报自动填写成功！您可以退出本程序了。')
        # print(ok)


def main():
    gui = GUI()


if __name__ == '__main__':
    main()
