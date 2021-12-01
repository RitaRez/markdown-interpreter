import unittest
from src.lexinterpreter import * 
  
class TestLexInterpreter(unittest.TestCase):

  def test_parse_bold_should_insert_html_tags(self):
    html = parse_bold("Here is a **bold** word")
    self.assertEqual(html, "Here is a <b>bold</b> word")

  def test_parse_italic_should_insert_html_tags(self):
    html = parse_italic("Here is an *italic* word")
    self.assertEqual(html, "Here is an <i>italic</i> word")

  def test_parse_link_should_insert_html_tags(self):
    html = parse_link("[test](https://test.com/)")
    self.assertEqual(html, "<a href=\"https://test.com/\">test</a>")

  def test_parse_ordered_list_should_insert_html_tags(self):
    html = parse_ordered_list("1. Rita\n2. Pedro\n")
    self.assertEqual(html, "<ol>\n<li>Rita</li>\n<li>Pedro</li>\n</ol>\n")

  def test_parse_unordered_list_should_insert_html_tags(self):
    html = parse_unordered_list("- Luiz\n- Alexis\n")
    self.assertEqual(html, "<ul>\n<li>Luiz</li>\n<li>Alexis</li>\n</ul>\n")
    html = parse_unordered_list("+ Luiz\n+ Alexis\n")
    self.assertEqual(html, "<ul>\n<li>Luiz</li>\n<li>Alexis</li>\n</ul>\n")
    html = parse_unordered_list("* Luiz\n* Alexis\n")
    self.assertEqual(html, "<ul>\n<li>Luiz</li>\n<li>Alexis</li>\n</ul>\n")

  def test_parse_header1_should_insert_html_tags(self):
    html = parse_header("# Header 1")
    self.assertEqual(html, "<h1>Header 1</h1>\n<hr>")

  def test_parse_header6_should_insert_html_tags(self):
    html = parse_header("###### Header 6")
    self.assertEqual(html, "<h6>Header 6</h6>\n<hr>")

  def test_parse_header7_should_fail_to_insert_html_tags(self):
    with self.assertRaises(ValueError):
      html = parse_header("####### Header 7")

  def test_parse_code1_should_insert_html_tags(self):
    html = parse_code("`Code here`")
    self.assertEqual(html, '<code style="background-color: #C2C2CF ; padding:2px; border-radius: 6px;" >Code here</code>')

  def test_parse_code3_should_insert_html_tags(self):
    html = parse_code("```Code here```")
    self.assertEqual(html, '<code style="background-color: #C2C2CF ; padding:2px; border-radius: 6px;" >Code here</code>')

