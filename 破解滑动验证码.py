from  selenium import webdriver





tiga=webdriver.Chrome()
tiga.get('https://passport.cnblogs.com/user/signin')
tiga.implicitly_wait(6)
try:

    #1.输入账号密码,点击登录
    username=tiga.find_element_by_id('input1')
    pwd=tiga.find_element_by_id('input2')
    btn=tiga.find_element_by_id('signin')

    username.send_keys('CTZ492745473')
    pwd.send_keys('CTZ1.2.3.DJATM')
    btn.click()

except Exception:
    pass
finally:
    tiga.close()
