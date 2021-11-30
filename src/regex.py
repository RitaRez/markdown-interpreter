import re

bold_token = r"\*\*(.*?)\*\*|\_\_(.*?)\_\_"
bold_result = r"<b>\g<1>\g<2></b>"

italic_token = r"\*(.*?)\*|\_(.*?)\_"
italic_result = r"<i>\g<1>\g<2></i>"

header_token = r"^(#+) (.*)$"
def header_result(type):
  return r"<h" + re.escape(str(type)) + r">\g<2></h" + re.escape(str(type)) + r">"