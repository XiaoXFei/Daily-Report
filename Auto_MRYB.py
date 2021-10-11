from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def main():
    filename = 'D:/PycharmProjects/user_infor.txt'
    print("*************************************************************")
    print("*                                                           *")
    print("*                                                           *")
    print("*                                                           *")
    print("*                                                           *")
    print("*                 欢迎使用sspu自动每日一报小程序               *")
    print("*                                                           *")
    print("*                                                           *")
    print("*                                                           *")
    print("*                                                           *")
    print("*                                                           *")
    print("*************************************************************")
    print("正在加载用户信息......")
    with open(filename) as f:
        tip = f.readline()
        username = f.readline().split()
        password = f.readline().split()
    f.close()
    print("正在打开浏览器........")
    b = webdriver.Chrome()
    b.get('https://id.sspu.edu.cn/cas/login?service=https%3a%2f%2fhsm.sspu.edu.cn%2fselfreport%2fLoginSSO.aspx'
          '%3ftargetUrl%3d%7bbase64%7daHR0cHM6Ly9oc20uc3NwdS5lZHUuY24vc2VsZnJlcG9ydC9JbmRleC5hc3B4')
    print("正在登录.............")
    time.sleep(1)
    # 填写账号密码
    b.find_element_by_id("username").send_keys(username)
    time.sleep(1)
    b.find_element_by_id("password").send_keys(password)
    time.sleep(1)
    # 点击登录
    b.find_element_by_class_name("submit_button").click()
    time.sleep(3)
    print("正在填写每日一报......")
    # 点击“每日一报”
    b.find_element_by_class_name("icos").click()
    time.sleep(1)
    # 点击“良好”
    b.find_element_by_id("fineui_2-inputEl-icon").click()
    time.sleep(1)

    # 输入体温
    temp_text = b.find_element_by_id("p1_TiWen")
    temp_text.click()
    time.sleep(3)

    temp_input = b.find_element_by_id("p1_TiWen-inputEl")
    temp_input.send_keys(Keys.CONTROL+'a')
    temp_input.send_keys(Keys.DELETE)
    time.sleep(2)

    b.find_element_by_id("fineui_37").click()
    time.sleep(1)
    temp_input.send_keys("36")
    # b.find_element_by_class_name("f-field-body-cell-centerpart").send_keys("37")

    time.sleep(2)
#f-tool-icon f-icon f-iconfont f-iconfont-close

    # 点击“点击提交”
    print("提交中...............")
    b.find_element_by_id("p1_ctl00_btnSubmit").click()

    time.sleep(3)
    # 点击“完成”
    b.find_element_by_id("fineui_39").click()
    time.sleep(1)
    print("每日一报自动提交完成！")
    print("程序自动关闭中........")
    time.sleep(1)
    # 关闭页面
    b.quit()


if __name__ == '__main__':
    main()