import unittest, time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType
from bs4 import BeautifulSoup

class SmokeTest(unittest.TestCase):
  def setUp(self):
    options = webdriver.FirefoxOptions()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)
    # self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.get("http://google.com")

  def tearDown(self):
    self.driver.quit()

  def test_google_returns_links(self):
    element = self.driver.find_element_by_name("q")
    element.send_keys("software testing")
    element.submit()
    time.sleep(3)

    html = self.driver.page_source
    parsed_html = BeautifulSoup(html, "html.parser")
        
    # TODO 1: encontrar os elementos "<div class="g">"
    links = parsed_html.body.find_all("div", class_="g")
    # TODO 2: assertGreater para garantir pelo menos 10 links
    self.assertGreater(len(links),10)