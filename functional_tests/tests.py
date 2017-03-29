
"""selenium test work"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NewVisitorTest(StaticLiveServerTestCase):
    """unit test"""
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # 맹과장이 업무 목록 앱을 사용하려고 한다.
        # 웹을 까본다.
        self.browser.get(self.live_server_url)

        # 웹페이지 타이틀과 헤더가 "To-Do"를 표시하고 있다.
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 새 작업을 추가해본다.
        inputbox = self.browser.find_element_by_id('item_text')
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
        mang_list_url = self.browser.current_url
        self.assertRegex(mang_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: 부장 뒷다마 까기')
        time.sleep(1)

        # 추가 아이템을 입력할 수 있는 여분의 텍스트상타자가 존재한다.
        inputbox = self.browser.find_element_by_id('item_text')
        # 다시 "이어서 본부장 뒷다마 까기"라고 입력한다. (맹과장은 꽤나 불만이 많은 사람이다.)
        inputbox.send_keys('본부장 뒷다마 까기')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        # 페이지는 다시 갱신되고, 두개 아이템이 목록에 보인다.
        self.check_for_row_in_list_table('2: 본부장 뒷다마 까기')
        self.check_for_row_in_list_table('1: 부장 뒷다마 까기')

        # 맹과장은 혹 누가 나중에 이걸 볼까 노심초사한다.
        # 사이트는 맹과장을 위한 URL을 생성해준다.
        # 이때 URL에 대한 설명도 함께 제공한다.

        # 해당 URL이 알려지면 맹과장은 전사적으로 까이게 된다.

        # 새로운 사용자인 송대리가 사이트에 접속한다.

        ## 새로운 브라우저 세션을 이용하여 에디스의 정보가 
        ## 쿠키를 통해 유입되는 것을 방지한다.
        time.sleep(1)
        self.browser.refresh()
        self.browser.quit()
        time.sleep(1)
        self.browser = webdriver.Firefox()

        # 송대리가 홈페이지에 접속한다.
        # 맹과장의 리스트는 보이지 않는다.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('부장 뒷다마 까기', page_text)
        self.assertNotIn('본부장 뒷다마 까기', page_text)

        # 송대리가 새로운 작업 아이템을 입력하기 시작한다.
        inputbox = self.browser.find_element_by_id('item_text')
        inputbox.send_keys('우유 사기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 송대리가 전용 URL을 취득한다.
        song_list_url = self.browser.current_url
        self.assertRegex(song_list_url, '/lists/.+')
        self.assertNotEqual(song_list_url, mang_list_url)

        # 맹과장이 입력한 흔적이 없다는 것을 다시 확인한다.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('부장 뒷다마 까기', page_text)
        self.assertIn('우유 사기', page_text)

        # 둘다 만족하고 끝난다.

        # self.fail('Finish the test!')

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element_by_id('item_text')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=50
        )
