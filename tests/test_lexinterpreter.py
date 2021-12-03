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

  # -------------------------- TESTS FOR STRIKED WORDS -------------------------- #

  def test_parse_strike_should_insert_html_tags(self):
    html = parse_strike("~~This is a mistake~~")
    self.assertEqual(html, "<s>This is a mistake</s>")

  def test_parse_strike_should_fail_because_of_line_break(self):
    html = parse_strike("~~This is a mistake \n~~")
    self.assertEqual(html, "~~This is a mistake \n~~")

   # -------------------------- TESTS FOR BOLD AND ITALIC WORDS -------------------------- #

  def test_parse_italic_and_bold_should_insert_html_tags(self):
    html = parse_bold("Here is an ***bold and italic*** word")
    html = parse_italic(html)
    self.assertEqual(html, "Here is an <b><i>bold and italic</b></i> word")

  def test_should_fail_to_parse_italic_bold_if_text_has_a_line_break(self):
    html = parse_bold("Here is a ***bold and italic\n*** word")
    html = parse_italic(html)
    self.assertEqual(html, "Here is a <i>*</i>bold and italic\n<i>*</i> word")

  # -------------------------- TESTS FOR STRIKED ITALIC AND BOLD WORDS -------------------------- #

  def test_parse_strike_italic_bold_should_insert_html_tags(self):
    html = parse_strike("~~***This is a mistake***~~")
    html = parse_bold(html)
    html = parse_italic(html)
    self.assertEqual(html, "<s><b><i>This is a mistake</b></i></s>")

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

    html = parse_bold("[__test__](https://test.com/)")
    html = parse_link(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><b>test</b></a>")

  def test_should_allow_italic_links(self):
    html = parse_link("[*test*](https://test.com/)")
    html = parse_italic(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><i>test</i></a>")

    html = parse_italic("[_test_](https://test.com/)")
    html = parse_link(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><i>test</i></a>")

  def test_should_allow_striked_links(self):
    html = parse_strike("[~~test~~](https://test.com/)")
    html = parse_link(html)
    self.assertEqual(html, "<a href=\"https://test.com/\"><s>test</s></a>")

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
    self.assertEqual(html, "<h1>Header 1</h1>")

  def test_parse_header6_should_insert_html_tags(self):
    html = parse_header("###### Header 6")
    self.assertEqual(html, "<h6>Header 6</h6>")

  def test_parse_header7_should_fail_to_insert_html_tags(self):
    html = parse_header("####### Header 7")
    self.assertEqual(html, "####### Header 7")

  def test_alternate_header_level1_should_insert_html_tags(self):
    html = parse_alternate_header("Heading level 1\n===============")
    self.assertEqual(html,"<h1>Heading level 1</h1>")

  def test_alternate_header_level2_should_insert_html_tags(self):
    html = parse_alternate_header("Heading level 2\n---------------")
    self.assertEqual(html,"<h2>Heading level 2</h2>")

  def test_alternate_header_level2_should_fail_to_insert_html_tags(self):
    html = parse_alternate_header("Heading level 2\n---------------1")
    self.assertEqual(html,"Heading level 2\n---------------1")

  # -------------------------- TESTS FOR CODE BITS -------------------------- #

  def test_parse_code_single_backsticks_should_insert_html_tags(self):
    html = parse_code("`Code here`")
    self.assertEqual(html, '<code style="background-color: #E3E6E8;" >Code here</code>')

  def test_parse_code_double_backsticks_should_insert_html_tags(self):
    html = parse_code("``Code here``")
    self.assertEqual(html, '<code style="background-color: #E3E6E8;" >Code here</code>')

  def test_parse_code_triple_backsticks_should_insert_html_tags(self):
    html = parse_code("```Code here```")
    self.assertEqual(html, '<code style="background-color: #E3E6E8;" >Code here</code>')

  # -------------------------- TESTS FOR BLOCKQUOTES -------------------------- #

  def test_parse_blockquote_should_insert_html_tags(self):
    html = parse_blockquote("> Meu quote")
    self.assertEqual(html, '<div style="width: 40%; height: 25px; background-color: gray"><div style="margin-left: 1%; width: 99%; height: 25px; background-color: #d0d7de;"><div style="padding-left: 1%; padding-top: 0.8%;" >Meu quote</div></div></div>')

  def test_parse_blockquote_should_fail(self):
    html = parse_blockquote(">Meu quote")
    self.assertEqual(html, ">Meu quote")

  def test_parse_should_allow_bold_and_striked_words_in_blockquotes(self):
    html = parse_blockquote("> **Meu** ~~quote~~")
    html = parse_bold(html)
    html = parse_strike(html)
    self.assertEqual(html, '<div style="width: 40%; height: 25px; background-color: gray"><div style="margin-left: 1%; width: 99%; height: 25px; background-color: #d0d7de;"><div style="padding-left: 1%; padding-top: 0.8%;" ><b>Meu</b> <s>quote</s></div></div></div>')

  def test_parse_should_allow_italic_links_in_blockquotes(self):
    html = parse_blockquote("> [*test*](https://test.com/)")
    html = parse_link(html)
    html = parse_italic(html)

    self.assertEqual(html, '<div style="width: 40%; height: 25px; background-color: gray"><div style="margin-left: 1%; width: 99%; height: 25px; background-color: #d0d7de;"><div style="padding-left: 1%; padding-top: 0.8%;" ><a href=\"https://test.com/\"><i>test</i></a></div></div></div>')

  

# -------------------------- TESTS FOR BREAKLINES AND PARAGRAPHS -------------------------- #

  def test_parse_breakline_should_insert_br_html_tag(self):
    html = parse_breakline("Just some nice text\r\nAnother line with text\r\nYet another line")
    self.assertEqual(html, "Just some nice text\r\n<br>\r\nAnother line with text\r\n<br>\r\nYet another line")

  def test_parse_of_paragraphs_should_insert_p_html_tag(self):
    html = parse_paragraph("Just some nice text")
    self.assertEqual(html, "<p>Just some nice text</p>")

  def test_parse_of_paragraphs_should_insert_two_p_html_tag(self):
    html = parse_paragraph("Just some nice text\nAnother nice text")
    self.assertEqual(html, "<p>Just some nice text</p>\n<p>Another nice text</p>")

  def test_parse_of_paragraphs_should_not_accept_empty_paragraphs(self):
    html = parse_paragraph("Just some nice text\n\nAnother nice text")
    self.assertEqual(html, "<p>Just some nice text</p>\n\n<p>Another nice text</p>")
  