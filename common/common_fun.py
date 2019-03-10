from kyb_testProject.baseView.baseView import BaseView
from kyb_testProject.common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
import logging.config
import os
import time
import xlrd
import csv

class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        logging.info('============check_cancelBtn===============')
        time.sleep(30)
        try:
            element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('updata element is not found')
        else:
            logging.info('click cancleBtn')
            element.click()

    def check_skipBtn(self):
        logging.info('============check_skiplBtn===============')
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('skip element is not found')
            #self.tap(867, 60, 1020, 147, 500)
            self.driver.tap([(867, 60),(1020, 147)], 500)
        else:
            logging.info('click skipBtn')
            element.click()

    def get_screen_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeLeft(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshot/%s_%s.png'%(module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        logging.info('============get_csv_data===============')
        with open(csv_file, 'r', encoding= 'utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == line:
                    return row


if __name__ == '__main__':
    # driver = appium_desired()
    # c = Common(driver)
    # c.check_cancelBtn()
    # c.check_skipBtn()
    # c.getScreenShot('startapp')
    # def get_excel_data(excel_file, sheet_name, line):
    #     data = []
    #     wb = xlrd.open_workbook(excel_file)
    #     sh = wb.sheet_by_name(sheet_name)
    #     for i in range(sh.nrows):
    #         d = sh.row_values(i)
    #         data.append(d)
    #
    #     for index, row in enumerate(data):
    #         if index == line:
    #             print(row)
    #
    # excel_file = '../data/account.xlsx'
    # sheet_name = 'Sheet1'
    # get_excel_data(excel_file, sheet_name, 2)

    def get_csv_data(csv_file, line):
        with open(csv_file, 'r', encoding= 'utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == line:
                    print(row)

    csv_file = '../data/account.csv'
    get_csv_data(csv_file, 2)

