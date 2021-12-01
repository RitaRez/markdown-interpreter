import unittest
from src.lexinterpreter import * 
  
class TestLexInterpreter(unittest.TestCase):

  # -------------------------- TESTS FOR BOLD WORDS -------------------------- #

  def test_parse_bold_should_insert_html_tags(self):
    html = parse_bold("Here is a **bold** word")
    self.assertEqual(html, "Here is a <b>bold</b> word")

    html = parse_bold("Here is a __bold__ word")
    self.assertEqual(html, "Here is a <b>bold</b> word")
  
  def test_parse_bold_should_not_accept_line_break(self):
    html = parse_bold("Here is a **bold\n** word")
    self.assertEqual(html, "Here is a **bold\n** word")

  # -------------------------- TESTS FOR ITALIC WORDS -------------------------- #

  def test_parse_italic_should_insert_html_tags(self):
    html = parse_italic("Here is an *italic* word")
    self.assertEqual(html, "Here is an <i>italic</i> word")

    html = parse_italic("Here is an _italic_ word")
    self.assertEqual(html, "Here is an <i>italic</i> word")

  def test_parse_italic_should_not_accept_line_break(self):
    html = parse_italic("Here is a *italic\n* word")
    self.assertEqual(html, "Here is a *italic\n* word")

  # -------------------------- TESTS FOR LINKS -------------------------- #

  def test_parse_link_should_insert_html_tags(self):
    html = parse_link("[test](https://test.com/)")
    self.assertEqual(html, "<a href=\"https://test.com/\">test</a>")

  def test_parsing_links_should_not_parse_images(self):
    html = parse_link("![alt description](https://test.com/image.jpg)")
    self.assertEqual(html, "![alt description](https://test.com/image.jpg)")

  def test_should_allow_bold_links(self):
    html = parse_link("[**test**](https://test.com/)")
    html = parse_bold(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><b>test</b></a>")

    html = parse_bold("[**test**](https://test.com/)")
    html = parse_link(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><b>test</b></a>")

  def test_should_allow_italic_links(self):
    html = parse_link("[*test*](https://test.com/)")
    html = parse_italic(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><i>test</i></a>")

    html = parse_italic("[*test*](https://test.com/)")
    html = parse_link(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><i>test</i></a>")

  def test_should_allow_list_of_links(self):
    html = "* [link 1](https://test.com/1)\n* [link 2](https://test.com/2)"
    html = parse_link(html)
    html = parse_unordered_list(html)
    self.assertEqual(html, "<ul>\n<li><a href=\"https://test.com/1\">link 1</a></li>\n<li><a href=\"https://test.com/2\">link 2</a></li>\n</ul>")

    html = "* [link 1](https://test.com/1)\n* [link 2](https://test.com/2)"
    html = parse_unordered_list(html)
    html = parse_link(html)
    self.assertEqual(html, "<ul>\n<li><a href=\"https://test.com/1\">link 1</a></li>\n<li><a href=\"https://test.com/2\">link 2</a></li>\n</ul>")

  def test_should_fail_to_parse_link_if_address_has_a_line_break(self):
    html = parse_image("[test](https://test\n.com/)")
    self.assertEqual(html, "[test](https://test\n.com/)")

  def test_should_fail_to_parse_link_if_text_has_a_line_break(self):
    html = parse_image("[test\nlink](https://test.com/)")
    self.assertEqual(html, "[test\nlink](https://test.com/)")

  def test_should_fail_to_parse_linnk_with_line_break_between_text_and_address(self):
    html = parse_image("[test]\n(https://test.com/)")
    self.assertEqual(html, "[test]\n(https://test.com/)")

  # -------------------------- TESTS FOR IMAGES -------------------------- #

  def test_parse_image_should_insert_html_tags(self):
    html = parse_image("![alt description](https://test.com/image.jpg)")
    self.assertEqual(html, "<img src=\"https://test.com/image.jpg\" alt=\"alt description\">")

  def test_should_fail_to_parse_image_if_path_has_a_line_break(self):
    html = parse_image("![alt description](https://test\n.com/image.jpg)")
    self.assertEqual(html, "![alt description](https://test\n.com/image.jpg)")

  def test_should_fail_to_parse_image_if_alt_has_a_line_break(self):
    html = parse_image("![alt\ndescription](https://test.com/image.jpg)")
    self.assertEqual(html, "![alt\ndescription](https://test.com/image.jpg)")

  def test_should_fail_to_parse_image_with_line_break_between_alt_and_path(self):
    html = parse_image("![alt description]\n(https://test.com/image.jpg)")
    self.assertEqual(html, "![alt description]\n(https://test.com/image.jpg)")

  # -------------------------- TESTS FOR LISTS -------------------------- #

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

  # -------------------------- TESTS FOR HEADERS -------------------------- #

  def test_parse_header1_should_insert_html_tags(self):
    html = parse_header("# Header 1")
    self.assertEqual(html, "<h1>Header 1</h1>\n<hr>")

  def test_parse_header6_should_insert_html_tags(self):
    html = parse_header("###### Header 6")
    self.assertEqual(html, "<h6>Header 6</h6>\n<hr>")

  def test_parse_header7_should_fail_to_insert_html_tags(self):
    html = parse_header("####### Header 7")
    self.assertEqual(html, "####### Header 7")

  # -------------------------- TESTS FOR CODE BITS -------------------------- #

  def test_parse_code1_should_insert_html_tags(self):
    html = parse_code("`Code here`")
    self.assertEqual(html, '<code style="background-color: #E3E6E8;" >Code here</code>')

  def test_parse_code3_should_insert_html_tags(self):
    html = parse_code("```Code here```")
    self.assertEqual(html, '<code style="background-color: #E3E6E8;" >Code here</code>')

