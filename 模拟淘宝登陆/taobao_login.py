import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# http://xiejava.ishareread.com/posts/6e762a1a/
class taobao_infos:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # 最大化窗口
        options.add_argument('--start-maximized')
        # 不加载图片,加快访问速度
        options.add_experimental_option("prefs",
                                        {"profile.managed_default_content_settings.images": 2,
                                         'credentials_enable_service': False,
                                         'profile.password_manager_enabled': False
                                         })
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 反爬虫特征处理(禁用 Chrome 浏览器中与自动化控制相关的特性，通常是为了规避某些网站对自动化测试或爬虫的检测)
        options.add_argument('--disable-blink-features=AutomationControlled')

        # 浏览器保持开启状态
        options.add_experimental_option('detach', True)

        chrome_service = Service(executable_path=chromedriver_path)
        self.browser = webdriver.Chrome(service=chrome_service, options=options)
        self.wait = WebDriverWait(self.browser, 20)  # 超时时长为10s
        self.chain = ActionChains(self.browser)  # 创建一个事件链对象

    # 判断元素是否存在
    def is_element_exist(self, element):
        try:
            self.browser.find_element(By.XPATH, element)
            return True
        except:
            return False

    def login(self, url):
        # 打开网址
        self.browser.get(url)

        # 等待用户名输入框加载完成，并模拟鼠标悬停
        input_login_id = self.wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))
        self.chain.move_to_element(input_login_id).perform()
        time.sleep(random.uniform(0.5, 1.0))  # 随机延迟
        # 分段输入用户名
        for char in username:
            input_login_id.send_keys(char)
            time.sleep(random.uniform(0.2, 0.4))  # 随机延迟
        # 等待密码输入框加载完成
        input_login_password = self.wait.until(EC.presence_of_element_located((By.ID, 'fm-login-password')))
        self.chain.move_to_element(input_login_password).perform()
        # 分段输入密码
        for char in password:
            input_login_password.send_keys(char)
            time.sleep(random.uniform(0.2, 0.4))
        time.sleep(1)

        # 判断滑块是否出现
        # while True:
        #     if self.is_element_exist("//div[@class='site-nav-user']"):
        #         print("登录成功")
        #         break;
        #     else:
        #         time.sleep(5)
        #         if self.is_element_exist():
        #             print("刷新滑块")
        #         else:
        #             print("拉动滑块")
        #     break

        print("获取滑块...")
        self.browser.implicitly_wait(3)  # 隐式等待5秒
        self.browser.switch_to.frame('baxia-dialog-content')
        js = 'Object.defineProperty(navigator,"webdriver",{get:()=>false,});'
        huakuai = self.wait.until(EC.presence_of_element_located((By.ID, 'nc_1_n1z')))
        self.browser.execute_script(js)

        # 找到拖动区域，获得宽高
        self.slide_to_right(huakuai)

        # 切换回窗口
        self.browser.switch_to.window(self.browser.window_handles[0])

        # 等待验证通过
        # self.wait.until(EC.text_to_be_present_in_element((
        #     By.CSS_SELECTOR, 'div#nc_1__scale_text > span.nc-lang-cnt > b'), '验证通过'
        # ))

        # 登陆
        print("准备登陆...")
        time.sleep(1)
        submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fm-button.fm-submit.password-login')))
        submit.click()

        # url是否改变
        # is_login = self.wait.until(EC.url_changes(url))

        # 关闭浏览器
        # self.browser.close()
        # self.browser.quit()

    def slide_to_right(self, huakuai):
        self.chain.click_and_hold(huakuai).perform()
        # 缓慢滑动
        i = 0
        step = 150
        # 模拟缓慢的滑动
        while i * step <= 378:
            print("移动...")
            self.chain.move_by_offset(step, 0).perform()
            i += 1
        # 释放滑块
        self.chain.release().perform()


if __name__ == '__main__':
    chromedriver_path = "H:/PycharmProjects/web-crawlers-example/drivers/chromedriver.exe"
    username = "001"  # 改成你的微博账号
    password = "002"  # 改成你的微博密码

    var = taobao_infos()
    var.login('https://login.taobao.com/member/login.jhtml')
