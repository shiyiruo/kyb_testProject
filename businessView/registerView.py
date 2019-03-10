from kyb_testProject.common.desired_caps import appium_desired
from kyb_testProject.common.common_fun import Common, By, NoSuchElementException
import logging
import random
from time import sleep


class RegisterView(Common):
    # 登录页，注册按钮
    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')
    # 头像设置相关元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')   # 添加头像
    item_image = (By.ID, 'com.tal.kaoyan:id/item_image')   # 头像image list
    saveBtn = (By.ID, 'com.tal.kaoyan:id/save')
    # 注册-个人信息元素
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')   # 用户名
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')   # 密码
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')   # 邮箱
    registerBtn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')   # 立即注册按钮
    # 完善信息页元素
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')   # 选择目标院校
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')   # 选择目标专业
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')   # 进入考研帮按钮
    #院校列表元素
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')   # 城市list
    university = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')   # 院校list
    #专业列表元素
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')
    # 个人中心元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')   # 用户名
    button_myself = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')   # 导航栏‘我‘

    def register_action(self, register_username, password, email):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('===============register start===============')
        self.driver.find_element(*self.register_text).click()   # 点击’注册‘
        # 添加保存头像
        # logging.info('set userheader')
        # self.driver.find_element(*self.userheader).click()  # 点击’添加头像‘
        # self.driver.find_elements(*self.item_image)[3].click()   # 选择并点击头像
        # #self.driver.find_element(*self.saveBtn).click()
        # self.driver.tap([(30, 1650), (330, 1794)], 500)
        # 填写用户名，密码，邮箱
        logging.info('register username is %s'%register_username)
        self.driver.find_element(*self.register_username).send_keys(register_username)
        logging.info('register password is %s'%password)
        self.driver.find_element(*self.register_password).send_keys(password)
        logging.info('register email is %s'%email)
        self.driver.find_element(*self.register_email).send_keys(email)
        logging.info('click register button')
        self.driver.find_element(*self.registerBtn).click()

        try:
            sleep(10)
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.info('register fail')
            self.getScreenShot('register fail')
            return False
        else:
            self.add_register_info()
            if self.check_register_status():
                return True
            else:
                return False

    def add_register_info(self):
        logging.info('===============add register info===============')
        logging.info('select school...')
        self.driver.find_element(*self.perfectinfomation_school).click()
        self.driver.find_elements(*self.forum_title)[1].click()
        self.driver.find_elements(*self.university)[1].click()
        self.driver.implicitly_wait(2)
        logging.info('select major...')
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.major_subject_title)[1].click()
        self.driver.find_elements(*self.major_group_title)[2].click()
        self.driver.find_elements(*self.major_search_item_name)[1].click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(*self.perfectinfomation_goBtn).click()

    def check_register_status(self):
        try:
            self.driver.find_element(*self.button_myself).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.info('register fail')
            self.getScreenShot('register fail')
            return False
        else:
            logging.info('register success')
            return True

if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)
    username = 'ceshi' + str(random.randint(100, 999))
    password = 'pass1234'
    email = str(random.randint(100000, 999999)) + '@qq.com'
    register.register_action(username, password, email)