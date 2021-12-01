from re import sub, search, subn
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

def parse_ordered_list(text):
  lines = text.split('\n')
  i = 0
  
  while i < len(lines):
    res = search(begining_list_token, lines[i])
    if res != None:
      lines.insert(i, '<ol>')
      i += 1
      lines[i] = sub(begining_list_token, result_list, lines[i]) # substituir por um elemento de lista
      while True:
        i += 1
        if i >= len(lines): break        
        res = search(generic_list_token, lines[i])
        if res != None:
          lines[i] = sub(generic_list_token, result_list, lines[i]) # substituir por um elemento de lista
        else:
          lines.insert(i, '</ol>')
          i += 1
          break
    else: 
      i += 1

  return '\n'.join(lines)

def parse_unordered_list(text):
  lines = text.split('\n')
  i = 0
  
  while i < len(lines):
    res = search(unorderd_list_token, lines[i])
    if res != None:
      lines.insert(i, '<ul>')
      i += 1
      lines[i] = sub(unorderd_list_token, result_list, lines[i]) # substituir por um elemento de lista
      while True:
        i += 1
        if i >= len(lines): break
        res = search(unorderd_list_token, lines[i])
        if res != None:
          lines[i] = sub(unorderd_list_token, result_list, lines[i]) # substituir por um elemento de lista
        else:
          lines.insert(i, '</ul>')
          i += 1
          break
    else: 
      i += 1

  return '\n'.join(lines)

def parse_code(text):
  return sub(code_token, code_result, text)

def parse_images(text):
  return sub(image_token, image_result, text)



def parse_text(markdown):
  markdown = parse_link(markdown)
  markdown = parse_images(markdown)
  markdown = parse_ordered_list(markdown)
  markdown = parse_unordered_list(markdown)
  markdown = parse_bold(markdown)
  markdown = parse_italic(markdown)
  markdown = parse_header(markdown)
  markdown = parse_code(markdown)
  return markdown
