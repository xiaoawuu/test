# print(sys.path)
from test_server.data import mysqls

'''
['C:\\test_server\\test_server',
 'C:\\test_server',
  'C:\\test_server\\bin\\test_port\\venv\\Scripts\\python37.zip',
   'C:\\install_file\\python3\\DLLs', 'C:\\install_file\\python3\\lib',
    'C:\\install_file\\python3', 'C:\\test_server\\bin\\test_port\\venv', 
    'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages', 
    'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages\\setuptools-40.8.0-py3.7.egg',
     'C:\\test_server\\bin\\test_port\\venv\\lib\\site-packages\\pip-19.0.3-py3.7.egg']
'''


def tests():
    print('------------')
    return True


# def test():
# 	list = ['LO-202008009374', 'LO-202008009375', 'LO-202008009376', 'LO-202008009377', 'LO-202008009378']
# 	dict = {}
# 	for i in list:
# 		print('循环：',i)
# 		sql = "SELECT freight_id FROM tms_wl_freight WHERE first_order_id ='{}';".format(i)
# 		data = mysqls.Data().query('tms_test', sql)
# 		dict[i] = data[0]['freight_id']
# 	return dict
# # print(max('4','0','1'))
#
# a= mysqls.Data().query('tms_test',"SELECT driver_day_count FROM tms_sys_order_limit WHERE c_id = (SELECT c_id FROM tms_wl_user WHERE user_name = 'AHD0285');")
#
# print(a)


# f = open("data1.txt","r")   #设置文件对象
# f.close() #关闭文件


# 为了方便，避免忘记close掉这个文件对象，可以用下面这种方式替代
# def read():
# 	print(123456789)
# 	data = '123456789asdf'
# 	try:
#
# 		with open('data.txt', "a", encoding="utf-8") as f:  # 设置文件对象
# 			f.write(str(data) + "\n")  # 可以是随便对文件的操作
# 			return True
# 	except Exception as e:
# 		return '异常：{}'.format(e)
# 	finally:
# 		f.close()


# read()

# 导入 base64模块
import base64

# 给定需要转换的字符串
str1 = "18007530111"

# 需要转成2进制格式才可以转换，所以我们这里再手动转换一下
result = base64.b64encode(str1.encode())

# 打印转换后的结果
# print('转换后的结果 -->  ',result)

# 再把加密后的结果解码7483
temp = base64.b64decode('MTE=')


# print(temp)

# 同样的，解码后的结0果是二进制，我们再转换一下
# print(temp.decode())
# A = base64.b64encode(temp.encode(encoding='utf8'))
# print(str(A, 'utf8'))
# read('ahuau')
def is_num_by_except(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def update_base64():
    # data = sql_select("SELECT id,recommend_mobile FROM biz_invite_code WHERE recommend_mobile LIKE 'MT%';")
    data = sql_select("SELECT id,recommend_mobile FROM biz_invite_code WHERE recommend_mobile != '' AND id > 7500;")
    for i in data:
        if not is_num_by_except(i[1]):
            try:
                temp = base64.b64decode(i[1].replace('\n', '').replace('\r', ''))
                sql_exec(
                    "UPDATE biz_invite_code SET recommend_mobile = '{}' WHERE id = {};".format(temp.decode(), i[0]))
                print(i[1], '转换为：', temp.decode())
            except:
                continue


# update_base64()

mobile = {}
import requests, json


def requestsPort(user_id, new_mobile):
    '''
    TP5修改手机号
    :param user_id:
    :param new_mobile:
    :return:
    '''
    # url=None
    url = "https://myadmin-api.zyb56.com/customer/changeUserMobile"
    re_data = {
        "token": "c1c95d62b91af8d7bb8e03a38e6b5215",
        "id": str(user_id),
        "mobile": new_mobile
    }
    try:
        headers = {
            "Content-Type": "application/json; charset=UTF-8"
        }
        response = requests.post(url, data=json.dumps(re_data), headers=headers)
        return response.json()
    except:
        return '异常'


from test_server.data.mysqls import Data


def updateMobile():
    for index, i in mobile.items():
        print('index:', index, "i", i)
        user_id = Data().query('zyb_live_r',
                               "SELECT id FROM `zyb_db`.`zyb_customer` WHERE `mobile` = '{}';".format(index))
        if user_id == ():
            continue
        print('user_id：', user_id[0]["id"], '旧手机号：', index, '新手机号：', i)
        print(requestsPort(user_id[0]["id"], i))


# updateMobile()
import datetime

# def getYesterday():
# 	yesterday = datetime.date.today() + datetime.timedelta(-1)
# 	return yesterday
# 输出
# print(getYesterday())

import time
# print()


import urllib, shutil
import glob, os
# from PIL import Image
import urllib.request
from test_server.data.sql import sql_select, sql_exec


class ImageDetection():
    def __init__(self):
        self.path = "C:\picture\\"
        self.path2 = "C:\picture\error\\"

    def isValid(self, file):
        '''
        工具：校验图片是否正常打开
        :param file:
        :return:
        '''
        try:
            Image.open(file).load()
        except OSError:
            return False
        return True

    def detectionPicture(self):
        paths = glob.glob(os.path.join(self.path, '*.jpg'))
        paths.sort()
        for path in paths:
            a = path[11:][:-4]
            is_true = self.isValid(path)
            if is_true == False:
                print(a)
            else:
                os.remove(path)

    def downloadImage(self, sql):
        '''
        下载图片
        :return:
        '''
        dataSQL = sql_select(sql)
        self.errList = []
        self.noneList = []
        for i in dataSQL:
            # print(i)
            if i[1][-9:] == "_zoom.png":
                url = 'http://app.juyuanpark.com' + i[1]
            else:
                url = 'http://app.juyuanpark.com' + i[1][:-10] + "_zoom.png"
            # print(url)
            try:
                request = urllib.request.Request(url)
                response = urllib.request.urlopen(request)
                get_img = response.read()
                # 图片下载至 C:\picture
                path = self.path + str(i[0]) + '.jpg'
                with open(path, 'wb') as fp:
                    fp.write(get_img)
                is_true = self.isValid(path)
                if is_true == False:
                    self.errList.append(i[0])
                    shutil.move(path, self.path2 + str(i[0]) + '.jpg')
            # shutil.copy2(path,self.path2 + str(i[0]) + '.jpg')
            # else:
            # 	os.remove(path)
            except:
                self.noneList.append(i[0])
                print('访问为空:{}'.format(i[0]))
                continue
        print('损坏的图片:')
        print(self.errList)
        print('为空的图片:')
        print(self.noneList)

    def headPortrait(self, sql):
        # list_a = []
        dataSQL = sql_select(sql)
        # print(dataSQL)
        for i in dataSQL:
            urls = i[1][:-4] + "_zoom.png"
            # print(urls)
            try:
                request = urllib.request.Request(urls)
                response = urllib.request.urlopen(request)
                get_img = response.read()
                # 图片下载至 C:\picture
                path = self.path + str(i[0]) + '.jpg'
                with open(path, 'wb') as fp:
                    fp.write(get_img)
                # print('图片下载完成：{}'.format(i[0]))
                is_true = self.isValid(path)
                # print('is_true',is_true)
                if is_true == False:
                    os.remove(path)
                else:
                    # updateSQL = "UPDATE biz_user SET picture = '{}' WHERE id = {};".format(urls[25:],i[0])
                    # sql_exec(updateSQL)
                    print(i[0])
                    print(urls)
            except:
                print('访问为空:{}'.format(i[0]))
                continue

    def photoAlbum(self, sql):
        list1 = []  # 都没有
        list2 = []  # 小图有
        list3 = []  # 大图有
        list4 = []  # 都图有
        dataSQL = sql_select(sql)
        for i in dataSQL:
            minUrl = 'http://app.juyuanpark.com' + i[1]
            maxUrl = 'http://app.juyuanpark.com' + i[2]
            try:

                request = urllib.request.Request(minUrl)
                response = urllib.request.urlopen(request)
                get_img = response.read()
                # 图片下载至 C:\picture
                path1 = self.path + 'min' + str(i[0]) + '.jpg'
                with open(path1, 'wb') as fp:
                    fp.write(get_img)
                is_true1 = self.isValid(path1)

                request = urllib.request.Request(maxUrl)
                response = urllib.request.urlopen(request)
                get_img = response.read()
                # 图片下载至 C:\picture
                path2 = self.path + 'max' + str(i[0]) + '.jpg'
                with open(path2, 'wb') as fp:
                    fp.write(get_img)
                is_true2 = self.isValid(path2)
                if is_true1 == True and is_true2 == True:
                    os.remove(path1)
                    os.remove(path2)
                elif is_true1 == True and is_true2 == False:
                    os.remove(path1)
                    list2.append(i[0])
                # sql_exec("UPDATE biz_album SET water_img_url = '{}' WHERE id = {};".format(i[1],i[0]))
                elif is_true1 == False and is_true2 == True:
                    os.remove(path2)
                    # sql_exec("UPDATE biz_album SET img_url = '{}' WHERE id = {};".format(i[2],i[0]))
                    list3.append(i[0])
                elif is_true1 == False and is_true2 == False:
                    # sql_exec('DELETE FROM biz_album WHERE id = {}'.format(i[0]))
                    list1.append(i[0])
            except:
                print('访问为空:{}'.format(i[0]))
                continue
        print('list1', list1)
        print('list2', list2)
        print('list3', list3)
        print('list4', list4)


# i = ImageDetection()
# i.a(sql)
# sql = "SELECT id,img FROM biz_social_img;"
# sql = "SELECT id,img_url FROM biz_album"
# sql = "SELECT id,water_img_url  FROM biz_album"
# sql = "SELECT id,picture  FROM biz_user"
# sql = "SELECT id,img FROM biz_social_img"
# i.downloadImage(sql)
# print("/Resources/UserPicture/19152/10d8c7ec23ac4704a84c1ebacc554c99.png")
# print("/Resources/UserPicture/19152/10d8c7ec23ac4704a84c1ebacc554c99.png"[-9:] )


'''
# os 模块
os.sep 可以取代操作系统特定的路径分隔符。windows下为 '\\'
os.name 字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是 'posix'
os.getcwd() 函数得到当前工作目录，即当前Python脚本工作的目录路径
os.getenv() 获取一个环境变量，如果没有返回none
os.putenv(key, value) 设置一个环境变量值
os.listdir(path) 返回指定目录下的所有文件和目录名
os.remove(path) 函数用来删除一个文件
os.system(command) 函数用来运行shell命令
os.linesep 字符串给出当前平台使用的行终止符。例如，Windows使用 '\r\n'，Linux使用 '\n' 而Mac使用 '\r'
os.path.split(path)  函数返回一个路径的目录名和文件名
os.path.isfile() 和os.path.isdir()函数分别检验给出的路径是一个文件还是目录
os.path.exists() 函数用来检验给出的路径是否真地存在
os.curdir  返回当前目录 ('.')
os.mkdir(path) 创建一个目录
os.makedirs(path) 递归的创建目录
os.chdir(dirname) 改变工作目录到dirname    
os.path.getsize(name) 获得文件大小，如果name是目录返回0L
os.path.abspath(name) 获得绝对路径
os.path.normpath(path) 规范path字符串形式
os.path.splitext()  分离文件名与扩展名
os.path.join(path,name) 连接目录与文件名或目录
os.path.basename(path) 返回文件名
os.path.dirname(path) 返回文件路径
os.walk(top,topdown=True,onerror=None)  遍历迭代目录
os.rename(src, dst)  重命名file或者directory src到dst 如果dst是一个存在的directory, 将抛出OSError. 在Unix, 如果dst在存且是一个file, 如果用户有权限的话，它将被安静的替换. 操作将会失败在某些Unix 中如果src和dst在不同的文件系统中. 如果成功, 这命名操作将会是一个原子操作 (这是POSIX 需要). 在 Windows上, 如果dst已经存在, 将抛出OSError，即使它是一个文件. 在unix，Windows中有效。
os.renames(old, new) 递归重命名文件夹或者文件。像rename()

# shutil 模块
shutil.copyfile( src, dst) 从源src复制到dst中去。当然前提是目标地址是具备可写权限。抛出的异常信息为IOException. 如果当前的dst已存在的话就会被覆盖掉
shutil.move( src, dst)  移动文件或重命名
shutil.copymode( src, dst) 只是会复制其权限其他的东西是不会被复制的
shutil.copystat( src, dst) 复制权限、最后访问时间、最后修改时间
shutil.copy( src, dst)  复制一个文件到一个文件或一个目录
shutil.copy2( src, dst)  在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst)  如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree( olddir, newdir, True/Flase)
把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.rmtree( src ) 递归删除一个目录以及目录内的所有内容

'''

import selenium
import time
from appium import webdriver

adevice = {
    "platformName": "Android",
    "platformVersion": "8.1.0",  # adb shell getprop ro.build.version.release
    "deviceName": "b649c4d",  # adb devices
    "appPackage": "com.fcx.jy",
    'newCommandTimeout': "3000",
    "automationName": "uiautomator2",
    "appActivity": "com.fcx.jy.ui.activity.LoginActivity"
}

'''
Find By	Selector
id	com.fcx.jy:id/tv_login
xpath	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[1]

Attribute	Value
index	0
text	登录
class	android.widget.TextView
package	com.fcx.jy
content-desc	
checkable	false
checked	false
clickable	true
enabled	true
focusable	true
focused	false
scrollable	false
long-clickable	true
password	false
selected	false
bounds	[45,1334][1035,1484]
resource-id	com.fcx.jy:id/tv_login
instance	0
'''

import os

print('selenium version = ', selenium.__version__)
# print('webdriver version = ', appium.__version__)
driver = webdriver.Remote('http://localhost:4723/wd/hub', adevice)
print(1)
time.sleep(1)

# time.sleep(1)
# driver.keyevent(4).

driver.find_element_by_id("com.fcx.jy:id/tv_login").click()

time.sleep(1)
driver.find_element_by_id("com.fcx.jy:id/edt_mobile").send_keys("18007530111")
time.sleep(1)
driver.find_element_by_id("com.fcx.jy:id/edt_code").send_keys("00000000")

driver.find_element_by_id("com.fcx.jy:id/tv_login").click()

time.sleep(1)
driver.find_element_by_id("com.fcx.jy:id/sousuo_view").click()
time.sleep(1)
driver.find_element_by_id('com.fcx.jy:id/sousuo_edt').send_keys('涵涵')
time.sleep(1)

time.sleep(1)
driver.find_element_by_id('com.fcx.jy:id/sousuo_edt').click()
time.sleep(1)
driver.press_keycode(66)
time.sleep(1)
# driver.press_keycode(66)
# driver.find_element_by_xpath(
#     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
# 坐标定位
a1 = 540 / 1944
b1 = 1080 / 2160
# 获取当前手机屏幕大小X,Y
X = driver.get_window_size()['width']
Y = driver.get_window_size()['height']
# 屏幕坐标乘以系数即为用户要点击位置的具体坐标	[45,1801][1035,1936]

driver.tap([(270, 255), (1050, 312)], 500)

time.sleep(1)
driver.tap([(540, 1943), (1080, 2160)], 500)
driver.find_element_by_id('com.fcx.jy:id/chat_message_input').send_keys('阿华')
time.sleep(1)
driver.find_element_by_id('com.fcx.jy:id/send_btn').click()

# driver.tap([(宽, 高), (分辨率)], 500)

print('exit!')

# driver.find_element_by_id("com.fcx.jy:id/rb_bt3").click()

'''
# driver.find_element_by_class_name("涵涵").click()
还是使用qq做为测试app，先通过start
recording生成python代码：

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from appium import webdriver

caps = {}
caps["deviceName"] = "e0a92c49"
caps["platformName"] = "Android"
caps["platformVersion"] = "4.4.4"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = "com.tencent.mobileqq.activity.SplashActivity"
# 不重置软件，通常用作保持登录状态
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 这里先使用time.sleep，更好的方式是用显式等待。
import time

time.sleep(2)

** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
可以把下面的定位方式的代码copy过来，直接执行
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
driver.quit()

下面介绍4种定位方式：

方式1：通过id定位（id精确匹配和模糊匹配都可以）
# 精确匹配id
el2 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
# 模糊匹配id
el2 = driver.find_element_by_id("btn_login")
el2.click()
# driver.find_element_by_xpath("")

方式2：通过class定位
在方式1中我们使用id定位到了登陆，这次我们模拟点击“新用户注册”，并使用class方式定位，由于class属性属于重复属性，也就是说不同的对象的class属性值可能一样，这就有可能在app界面里找到多个匹配的对象，例如（如图）：qq登陆和新用户这两个按钮的class属性都是：android.widget.Button。

那么怎么区别这两个按钮呢，实现方式：使用“driver.find_elements_by_class_name”, 注意elements用复数形式，取到下标，找到该对象。代码如下：
elements = driver.find_elements_by_class_name("android.widget.Button")
print(elements)
运行结果如下：

由于“新用户”的按钮下标是1，所以我们使用[1]
来取到“新用户”按钮
elements = driver.find_elements_by_class_name("android.widget.Button")[1]
elements.click()

方式3：通过xpath定位，模拟登录
element = driver.find_element_by_xpath("//android.widget.Button[@text='登 录']")
element.click()
说明：
使用xpath属性时，推荐使用不受影响的xpath属性，如下图，在本案里，应该使用content - desc属性
方式4：通过accessibility_id定位，模拟登录
element = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
element.send_keys('1728731231')

彩蛋：如果执行的时候出现We
wanted
{"required": ["value"]} and you
sent["text", "sessionId"]
解决方法1：降级selenium为3
.3
.1
解决方法2：使用setvalue
api代替

方式5：android特有的定位方式，通过ui - automator - selector
element = driver.find_elements_by_android_uiautomator('new UiSelector().text("登 录")')

'''
