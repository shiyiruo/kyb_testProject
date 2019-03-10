from kyb_testProject.common.desired_caps import appium_desired
from kyb_testProject.common.common_fun import Common, By
from selenium.common.exceptions import NoSuchElementException
import logging

class LoginView(Common):
    # 登录页面元素
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')   # 用户名输入框
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')   # 密码输入框
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')   # 登录按钮
    # 个人中心元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')   # 用户名
    button_myself = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')   # 导航栏‘我‘
    #退登元素
    settingBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButtonWraper')   # 设置按钮
    logoutBtn = (By.ID,'com.tal.kaoyan:id/setting_logout_text')   # 退出登录按钮
    tip_commit = (By.ID,'com.tal.kaoyan:id/tip_commit')   # 确认退登按钮

    def login_action(self, username, password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('===============login start===============')
        logging.info('input username %s'%username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info('input password %s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)
        self.driver.find_element(*self.loginBtn).click()
        logging.info('===============login end===============')

    def check_loginStatus(self):
        try:
            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login fail')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('===============logout start===============')
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()
        logging.info('===============logout end===============')

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('自学网2017','zxw2017')
    l.check_loginStatus()