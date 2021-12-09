import unittest, time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

class AcceptanceTest(unittest.TestCase):
  def setUp(self):
    options = webdriver.FirefoxOptions()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)
    self.driver.get("https://ritarez.github.io/markdown-interpreter/")

  def tearDown(self):
    self.driver.quit()

  def test_source_code_is_obtainable(self):
    source_code_link = self.driver.find_element(By.XPATH, '//*[@id="page-header"]/p/a')
    self.assertEqual(source_code_link.get_attribute('href'), 'https://github.com/RitaRez/markdown-interpreter')

  def test_converting_list_should_return_li_elements(self):
    markdown_text_area = self.driver.find_element(By.ID, 'markdown-textarea')
    markdown_text_area.send_keys('1. elemento 1\n2. elemento 2\n3. elemento 3')
    
    convert_btn = self.driver.find_element(By.ID, 'preview-button')
    convert_btn.click()

    time.sleep(3)

    list_elements = self.driver.find_element(By.ID, 'preview-container').find_elements(By.TAG_NAME, 'li')
    for idx, el in enumerate(list_elements):
      self.assertEqual(el.text, 'elemento ' + str(idx+1))

  def test_converting_headers_should_return_htags(self):
    markdown_text_area = self.driver.find_element(By.ID, 'markdown-textarea')
    markdown_text_area.send_keys('# Big Title\n## Medium title\n### Small title')
    
    convert_btn = self.driver.find_element(By.ID, 'preview-button')
    convert_btn.click()

    time.sleep(3)

    converted_html = self.driver.find_element(By.ID, 'preview-container')
    first_header = converted_html.find_element(By.TAG_NAME, 'h1')
    self.assertEqual(first_header.text, 'Big Title')
    
    second_header = converted_html.find_element(By.TAG_NAME, 'h2')
    self.assertEqual(second_header.text, 'Medium title')
    
    third_header = converted_html.find_element(By.TAG_NAME, 'h3')
    self.assertEqual(third_header.text, 'Small title')

  def test_converting_headers_should_return_htags(self):
    markdown_text_area = self.driver.find_element(By.ID, 'markdown-textarea')
    markdown_text_area.send_keys('# Big Title\n## Medium title\n### Small title')
    
    convert_btn = self.driver.find_element(By.ID, 'preview-button')
    convert_btn.click()

    time.sleep(3)

    converted_html = self.driver.find_element(By.ID, 'preview-container')
    first_header = converted_html.find_element(By.TAG_NAME, 'h1')
    self.assertEqual(first_header.text, 'Big Title')
    
    second_header = converted_html.find_element(By.TAG_NAME, 'h2')
    self.assertEqual(second_header.text, 'Medium title')
    
    third_header = converted_html.find_element(By.TAG_NAME, 'h3')
    self.assertEqual(third_header.text, 'Small title')

    
