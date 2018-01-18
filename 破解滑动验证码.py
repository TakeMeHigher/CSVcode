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
    #image_obj.show()
    return image_obj

def get_distance(image1,image2):
    start_x=58
    threhold=60
    print(image1.size)#(258, 159)
    print(image2.size)#(258, 159)
    for x in range(start_x,image1.size[0]):
        for y in range(image1.size[1]):
            rgb1=image1.load()[x,y]
            rgb2=image2.load()[x,y]

            res1=abs(rgb1[0]-rgb2[0])
            res2=abs(rgb1[1]-rgb2[1])
            res3=abs(rgb1[2]-rgb2[2])
            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                return x-7


def get_tracks(distance):
    distance+=20
    #v=v0+a*t
    #s=v*t+0.5*a*(t**2)

    v0=0
    s=0
    t=0.2
    mid=distance*3/5
    forward_tracks=[]

    while s < distance:
        if s < mid:
            a=2
        else:
            a=-3

        v=v0
        track=v*t+0.5*a*(t**2)
        track=round(track)
        v0=v+a*t
        s+=track
        forward_tracks.append(track)
    back_tracks=[-1,-1,-1,-2,-2,-2,-3,-3,-2,-2,-1] #20
    return {"forward_tracks":forward_tracks,'back_tracks':back_tracks}





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

    #6、对比两张图片，找出缺口，即滑动的位移
    distance=get_distance(image1,image2)
    print(distance)

    # 7、按照人的行为行为习惯，把总位移切成一段段小的位移
    traks_dic = get_tracks(distance)



    

    time.sleep(10)

except Exception:
    pass
finally:
    tiga.close()
