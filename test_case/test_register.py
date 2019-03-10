from kyb_testProject.common.myunit import StartEnd
from kyb_testProject.businessView.registerView import RegisterView
import logging
import random
import unittest

class RegisterTest(StartEnd):

    def test_user_register(self):
        logging.info('=========test_user_register======')
        r = RegisterView(self.driver)
        username = 'ceshi' + str(random.randint(100, 999))
        password = 'pass1234'
        email = str(random.randint(100000, 999999)) + '@qq.com'
        self.assertTrue(r.register_action(username, password, email))

if __name__ == '__main__':
    unittest.main()