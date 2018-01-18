import  time

from  selenium import webdriver
from PIL import Image



def get_snap(tiga):
    tiga.save_screenshot('snap.png')
    snap_obj=Image.open('snap.png')
    return snap_obj




def get_img(tiga):
    complete_img=tiga.find_element_by_class_name('geetest_canvas_img')
    time.sleep(2)
    size=complete_img.size
    location=complete_img.location
    left=location['x']
    top=location['y']
    right=left+size['width']
    bottom=top+size['height']

    snap_obj=get_snap(tiga)
    image_obj = snap_obj.crop((left, top, right, bottom))
    image_obj.show()
    return image_obj




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

    #2.点击按钮弹出没有切口的图
    button=tiga.find_element_by_class_name('geetest_radar_tip')
    button.click()


    #3.针对没有切口的图进行截图
    image1=get_img(tiga)

    # 4、点击滑动按钮，弹出有缺口的图
    slider_button=tiga.find_element_by_class_name('geetest_slider_button')
    slider_button.click()

    # 5、针对有缺口的图片进行截图
    image2=get_img(tiga)

    time.sleep(10)

except Exception:
    pass
finally:
    tiga.close()
