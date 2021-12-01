bold_token = r'\*\*(.*?)\*\*|\_\_(.*?)\_\_'
bold_result = r'<b>\g<1>\g<2></b>'

italic_token = r'\*(.*?)\*|\_(.*?)\_'
italic_result = r'<i>\g<1>\g<2></i>'

header_token = r'^(#+) (.*)$'
def header_result(type):
  return r'<h' + str(type) + r'>\g<2></h' + str(type) + r'>\n<hr>'

link_token = r'\[(.*?)\] *\((.*?)\)'
link_result = r'<a href="\g<2>">\g<1></a>'

begining_list_token = r'^(1. )'
generic_list_token = r'^([0-9]. )'
unorderd_list_token = r'^([-|*|+] )'

code_token = r'\`\`\`(.*?)\`\`\`|\`\`(.*?)\`\`|\`(.*?)\`'
code_result = r'<code style="background-color: #C2C2CF ; padding:2px; border-radius: 6px;" >\g<1>\g<2>\g<3></code>'