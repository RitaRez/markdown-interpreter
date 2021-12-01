from re import sub, search
from src.regex import *

def parse_bold(text):
  return sub(bold_token, bold_result, text)

def parse_italic(text):
  return sub(italic_token, italic_result, text)

def parse_header(text):
  lines = text.split('\n')

  for i in range(len(lines)):
    line = lines[i]
    res = search(header_token, line)
    if res != None:
      header_type = len(res.group(1))
      if(header_type <= 6):
        lines[i] = sub(header_token, header_result(header_type), line)
      else:
        raise ValueError("Amount of headers is not standard")

  return '\n'.join(lines)

def parse_link(text):
  return sub(link_token, link_result, text)

def parse_text(markdown):
  markdown = parse_link(markdown)
  markdown = parse_bold(markdown)
  markdown = parse_italic(markdown)
  markdown = parse_header(markdown)
  return markdown