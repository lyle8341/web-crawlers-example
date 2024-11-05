from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class slide:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs",
                                        {"profile.managed_default_content_settings.images": 2,
                                         'credentials_enable_service': False,
                                         'profile.password_manager_enabled': False
                                         })
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('detach', True)

        chrome_service = Service(executable_path=chromedriver_path)
        self.browser = webdriver.Chrome(service=chrome_service, options=options)
        self.wait = WebDriverWait(self.browser, 20)  # 超时时长为10s
        self.slide = ActionChains(self.browser)  # 启动滑动功能

    def login(self, url):
        self.browser.get(url)
        huakuai = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.handler.handler_bg')))
        self.slide.click_and_hold(huakuai).perform()  # 按住滑块
        i = 0
        step = 10
        # 模拟缓慢的滑动
        while i * step <= 260:
            self.slide.move_by_offset(step, 0).perform()
            i = i + 1
        # 释放滑块
        self.slide.release().perform()

        # 等待验证通过
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div#drag > div.drag_text'), '验证通过'))
        print("验证通过")
        self.browser.quit()


if __name__ == '__main__':
    chromedriver_path = "H:/PycharmProjects/web-crawlers-example/drivers/chromedriver.exe"
    var = slide()
    var.login('file:///C:/Users/Dragon-PC/AppData/Roaming/JetBrains/PyCharm2021.2/scratches/scratch_2.html')  # 登录
