
"""selenium test work"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    """unit test"""
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # 맹과장이 업무 목록 앱을 사용하려고 한다.
        # 웹을 까본다.
        self.browser.get("http://localhost:8000")

        # 웹페이지 타이틀과 헤더가 "To-Do"를 표시하고 있다.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 새 작업을 추가해본다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업아이템입력'
        )

        # "부장 뒷다마 까기"를 텍스트 상자에 입력한다.
        inputbox.send_keys('부장 뒷다마 까기')

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1: 부장 뒷다마 까기" 아이템이 추가된다.
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        # 추가 아이템을 입력할 수 있는 여분의 텍스트상타자가 존재한다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        # 다시 "이어서 본부장 뒷다마 까기"라고 입력한다. (맹과장은 꽤나 불만이 많은 사람이다.)
        inputbox.send_keys('본부장 뒷다마 까기')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        # 페이지는 다시 갱신되고, 두개 아이템이 목록에 보인다.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: 부장 뒷다마 까기', [row.text for row in rows])
        self.assertIn('2: 본부장 뒷다마 까기', [row.text for row in rows])

        # 맹과장은 혹 누가 나중에 이걸 볼까 노심초사한다.
        # 사이트는 맹과장을 위한 URL을 생성해준다.
        # 이때 URL에 대한 설명도 함께 제공한다.

        # 해당 URL이 알려지면 맹과장은 전사적으로 까이게 된다.

        # 삭제 방법을 개발자에 묻기도 하고 불안에 떨면 사이트를 닫는다.
        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main(warnings='ignore')
