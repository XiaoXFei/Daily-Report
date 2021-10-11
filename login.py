import tkinter as tk
import tkinter.messagebox

import pymysql

root = tk.Tk()
root.title('登录')
root.geometry('500x300')

canvas = tk.Canvas(root,width=500,height=114)
image_file = tk.PhotoImage(file='jike.gif')
image = canvas.create_image(250,0,anchor='n',image=image_file)
canvas.pack(side='top')
tk.Label(root,text='wellcome',font=('Arial',16)).pack()

tk.Label(root,text='账户:',font=('Arial',14)).place(x=50,y=150)
tk.Label(root,text='密码:',font=('Arial',14)).place(x=50,y=190)

var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(root,textvariable=var_usr_name,font=('Arial',14))
entry_usr_name.place(x=160,y=155)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(root, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=160,y=192)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    db = pymysql.connect('localhost','root','mc123456','Northwind',charset='utf8') # 数据库设置
    cursor = db.cursor()
    sql_verify = """SELECT table_name FROM information_schema.TABLES t 
    WHERE t.table_schema='Northwind' and t.table_name ='users'"""
    if cursor.execute(sql_verify):
        print('users表已存在')
    else:
        sql_createtable = """
            create table users(
            account char(20) not null,
            password char(20) not null,
            age int,
            sex char(1))
        """
        cursor.execute(sql_createtable)
    search_sql = 'select account,password from users where account=%s'%usr_name
    try:   
        if cursor.execute(search_sql):
            usr = cursor.fetchone()
            if usr_pwd == usr[1]:
                tkinter.messagebox.showinfo(title='welcome',message='how are you?'+usr_name)
            else:
                tkinter.messagebox.showerror(title='error',message='密码输入错误')
        else:
            is_sign_up = tkinter.messagebox.askyesno('welcome','该用户未注册，是否注册')
            if is_sign_up:
                usr_sign_up()
    except:
        print('非法字符')
    db.close()

def usr_sign_up():
    def sign_to_website():
        new_usr_account = entry_new_account.get()
        new_usr_pwd = entry_usr_pwd.get()
        new_usr_pwd_c = entry_usr_pwd_confirm.get()
        if new_usr_pwd != new_usr_pwd_c:
            tkinter.messagebox.showerror(title='error',message='两次密码必须一致')
        else:
            db = pymysql.connect('localhost','root','mc123456','Northwind',charset='utf8')
            cursor = db.cursor()
            sql_search='select * from users where account=%s'%new_usr_account
            if cursor.execute(sql_search):
                tkinter.messagebox.showerror(title='error',message='该用户已经注册')
            else:
                sql_insert="insert into users(account,password) values(%s,%s)"%(new_usr_account,new_usr_pwd)
                try:
                    cursor.execute(sql_insert)
                    db.commit()
                    tkinter.messagebox.showinfo('welcome','注册成功')
                    sign_up_window.destroy()
                except:
                    db.rollback()

    sign_up_window = tk.Toplevel(root)
    sign_up_window.geometry('320x180')
    sign_up_window.title('注册')

    new_usr_account = tk.StringVar()
    tk.Label(sign_up_window,text='账户名:').place(x=30,y=10)
    entry_new_account = tk.Entry(sign_up_window,textvariable=new_usr_account)
    entry_new_account.place(x=130,y=10)

    new_usr_pwd = tk.StringVar()
    tk.Label(sign_up_window,text='密码:').place(x=30,y=50)
    entry_usr_pwd = tk.Entry(sign_up_window,textvariable=new_usr_pwd,show='*')
    entry_usr_pwd.place(x=130,y=50)

    new_usr_pwd_c = tk.StringVar()
    tk.Label(sign_up_window,text='密码确认:').place(x=30,y=90)
    entry_usr_pwd_confirm = tk.Entry(sign_up_window,textvariable=new_usr_pwd_c,show='*')
    entry_usr_pwd_confirm.place(x=130,y=90)

    btn_comfirm_sign_up = tk.Button(sign_up_window,text='注册',command=sign_to_website)
    btn_comfirm_sign_up.place(x=180,y=130)

btn_login = tk.Button(root,text='login',command=usr_login)       
btn_login.place(x=180,y=240)
btn_sign_up = tk.Button(root, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=240, y=240)

root.mainloop()