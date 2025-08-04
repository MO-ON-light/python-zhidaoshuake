print('*****************************')
print('*****这是知到的自动刷课脚本******')
print('*****************************')
print('在初次点击课堂听课时，会有个人诚信声明，请自行点击确认，为自己的行为负责;若没有，不必理会此条提醒。')
print('在初次点击课堂听课时，会有个人诚信声明，请自行点击确认，为自己的行为负责;若没有，不必理会此条提醒。')
print('在初次点击课堂听课时，会有个人诚信声明，请自行点击确认，为自己的行为负责;若没有，不必理会此条提醒。')
input("\n点击回车键，确认继续！")
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import threading
import time

edge_option = Options()
edge_option.add_argument("--no-sandbox")
edge_option.add_experimental_option("detach",True)
edge_option.add_argument("--disable-blink-features=AutomationControlled")
edge_option.add_experimental_option("excludeSwitches",['enable-automation'])
edge_option.add_argument('--log-level=3')
edge_option.add_argument('--disable-logging')
edge_option.add_experimental_option('excludeSwitches', ['enable-logging'])

open_edge = webdriver.Edge(service=Service('msedgedriver.exe'),options=edge_option)
open_edge.minimize_window()
open_edge.get('https://onlineweb.zhihuishu.com/onlinestuh5')

print('\n*****请选择登录方式*****')
print('使用提醒:')
print('若是账号密码登录，安全验证请自行完成!!!\n其他之外的东西不要动!!!')
print('[0]账号密码登录\n[1]微信扫码登录\n[2]知到扫码登录\n')
login_num = int(input('操作选择:'))
try:
    if login_num == 0:
        print('\n账号密码登录')
        print('记得自行完成安全验证')
        id = int(input('请输入手机号:'))
        psd =input('请输入密码:')
        open_edge.maximize_window()
        time.sleep(1)
        open_edge.find_element(By.XPATH, '//*[@id="lUsername"]').send_keys(f'{id}')
        time.sleep(1)
        open_edge.find_element(By.XPATH, '//*[@id="lPassword"]').send_keys(f'{psd}')
        time.sleep(1)
        open_edge.find_element(By.XPATH, '//*[@id="f_sign_up"]/div[1]/span').click()
        open_edge.implicitly_wait(60)
        if(open_edge.find_element(By.XPATH,'//*[@id="form-ipt-error-l-username"]').text == '手机号或密码错误'):
            open_edge.minimize_window()
            print('手机号或密码错误')
            exit(0)
        else:
            open_edge.find_element(By.XPATH, '//*[@id="dif_v1"]/div/div')#个人首页
    elif login_num == 1:
        print('\n微信扫码登录\n')
        open_edge.maximize_window()
        try:
            open_edge.implicitly_wait(120)
            open_edge.find_element(By.XPATH,'//*[@id="headerMain"]/ul/li[4]/a').click()
        except:
            print('登录超时')
    elif login_num == 2:
        print('\n知到扫码登录\n')
        open_edge.maximize_window()
        open_edge.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[2]').click()
        open_edge.implicitly_wait(120)
        try:
            open_edge.find_element(By.XPATH, '//*[@id="headerMain"]/ul/li[4]/a').click()
        except:
            pass
        finally:
            open_edge.find_element(By.XPATH, '//*[@id="dif_v1"]/div/div/div[1]/a/img')
except:
    print('\n数字不符合要求！！！请输入[]内的数字！！！\n')
    exit(0)

#课程开始
open_edge.minimize_window()
time.sleep(1)
print('\n正在扫描课程与进度...')
#扫描课程与进度，进行选择
def course():
    time.sleep(1)
    all_course = open_edge.find_elements(By.XPATH,'//*[@id="sharingClassed"]/div[2]/ul/div/dl/dt/div[1]/div[1]')#所有课程
    all_progress = open_edge.find_elements(By.XPATH,'//*[@id="sharingClassed"]/div[2]/ul/div/dl/dt/div[1]/div[3]/div[2]/span[2]')#所有进度
    a_time = []
    for i in range(0,len(all_course)):
        a_time.append(i)#等待元素加载
        print(f'[{i}]{all_course[i].text}--{all_progress[i].text}')#0开始
    course_num = int(input('请输入[]内的数字,选择将要学习的课程:'))
    # 点击课堂
    if (course_num <= a_time[-1]):
        open_edge.find_element(By.XPATH, f'//*[@id="sharingClassed"]/div[2]/ul[{course_num+1}]/div/dl/dt/div[1]/div[1]').click()
    else:
        print("数字不符合要求！！！请输入[]内的数字！！！")
        exit(0)

time.sleep(1)
course()
open_edge.maximize_window()

open_edge.implicitly_wait(180)#个人诚信确认
time.sleep(1)
print('\n已开始自动学习,代码执行中...\n\n除了安全验证以外，请勿打断代码执行!!!')
try:#广告
    open_edge.implicitly_wait(2)
    open_edge.find_element(By.XPATH,'//*[@id="app"]/div/div[9]/div/div[2]/div/div[3]/div[1]').click()
except:
    pass

# open_edge.minimize_window()
m = WebDriverWait(open_edge,2,0.5)
wait = WebDriverWait(open_edge,7200,0.5)
#操作暂停、关闭声音
class Movement:
    @staticmethod
    def play():
        q = m.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="playButton"]')))
        q.click()#播放键

    @staticmethod
    def next():
        w = m.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="nextBtn"]')))
        w.click()

    @staticmethod
    def close_voice():
        e = m.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="vjs_container"]/div[10]/div[7]/div[1]')))
        e.click() # 关闭音量


event1 = threading.Event()#主
event2 = threading.Event()#子

def alert():#进程执行窗口问题
    try:
        open_edge.implicitly_wait(1)
        open_edge.find_element(By.XPATH, '//*[@id="playTopic-dialog"]/div') # 问题弹窗
        action = ActionChains(open_edge)
        element1 = open_edge.find_element(By.XPATH,'//svg[@class="icon topic-option"]')
        element2 = open_edge.find_element(By.XPATH,'//button[@class="el-dialog__headerbtn"]')
        action.click(element1)
        action.click(element2)
    except TimeoutException:
        open_edge.implicitly_wait(1)
        open_edge.find_element(By.XPATH, '//div[@class="yidun_modal__header"]')
        WebDriverWait(open_edge, 86400, 0.5).until_not(ec.presence_of_element_located((By.XPATH, '//div[@class="yidun_modal__header"]')))
    except NoSuchElementException:#没运行这个
        pass
    time.sleep(0.1)

def enter():
    open_edge.find_element(By.XPATH, '//*[@id="app"]/div/div[6]/div[2]/div[1]/i').click()  # 弹窗
    open_edge.implicitly_wait(3)
    all_finish = open_edge.find_elements(By.XPATH, '//li[contains(@class,"clearfix video")]//b[@class="fl time_icofinish"]')
    n = len(all_finish)
    open_edge.implicitly_wait(2)
    open_edge.find_elements(By.XPATH, '//b[@class="time_ico_half fl"]')[n].click()  # 点击没播放的视频
    print('静音')
    Movement.close_voice()
    print('播放')
    Movement.play()

def watch():
    while True:
        event2.wait()
        try:
            open_edge.implicitly_wait(2)
            open_edge.find_element(By.XPATH, '//li[@class="clearfix video current_play//b[@class="fl time_icofinish"]')
            Movement.next()
            Movement.close_voice()
            Movement.play()
        except:
            pass
        event2.clear()
        event1.set()


alert()
#进入课堂
enter()

thread = threading.Thread(target=watch,daemon=True).start()
all_courses = open_edge.find_elements(By.XPATH, '//li[contains(@class,"clearfix video")]')
all_finish = open_edge.find_elements(By.XPATH, '//li[contains(@class,"clearfix video")]//b[@class="fl time_icofinish"]')

event1.set()
while True:
    if (len(all_courses) == len(all_finish)):
        open_edge.quit()
        print('已完成所有的课程')
        break
    else:
        event1.wait()
        alert()
        event1.clear()
        event2.set()
