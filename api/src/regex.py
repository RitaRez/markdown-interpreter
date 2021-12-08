bold_token = r'\*\*(.+?)\*\*|\_\_(.+?)\_\_'
bold_result = r'<b>\g<1>\g<2></b>'

italic_token = r'\*(.+?)\*|\_(.+?)\_'
italic_result = r'<i>\g<1>\g<2></i>'

header_token = r'^(#{1,6}) (.*)$'
def header_result(type):
  return r'<h' + str(type) + r'>\g<2></h' + str(type) + r'>'

link_token = r'(^|[^!])\[(.*?)\] *\((.*?)\)'
link_result = r'\g<1><a href="\g<3>">\g<2></a>'

image_token = r'!\[(.*?)\] *\((.*?)\)'
image_result = r'<img src="\g<2>" alt="\g<1>">'

breakline_token = r'(\r\n)|(\r)|(\n)'
breakline_result = r'\g<1>\g<2>\g<3><br>\g<1>\g<2>\g<3>'

paragraph_token = r'^( *(?!(<h[1-6]>)|(</?ul>)|(</?ol>)|(</?li>)|(</?tr>)|(</?table>)|(</?td>)|(</?th>)).+?)$'
paragraph_result = r'<p>\g<1></p>'

begining_list_token = r'^1\. (.*)'
generic_list_token = r'^[0-9]\. (.*)'
unorderd_list_token = r'^[-*+] (.*)'
result_list = r'<li>\g<1></li>'

code_token = r'(```((.|\n)*?)```)|(``((.|\n)*?)``)|(`((.|\n)*?)`)'
code_result = r'<code style="background-color: #E3E6E8;" >\g<2>\g<5>\g<8></code>'

strike_token = r'~~(.+?)~~'
strike_result = r'<s>\g<1></s>'

blockquote_token = r'^> (.+)'
blockquote_result = r'<div style="width: 40%; height: 25px; background-color: gray"><div style="margin-left: 1%; width: 99%; height: 25px; background-color: #d0d7de;"><div style="padding-left: 1%; padding-top: 0.8%;" >\g<1></div></div></div>'

alternate_header_token_level1 = r'(^\=\=*$)'

alternate_header_token_level2 = r'(^\-\-*$)'