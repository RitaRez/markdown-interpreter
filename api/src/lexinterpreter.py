from re import sub, search, subn, match
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
      lines[i] = sub(header_token, header_result(header_type), line)

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
        if i >= len(lines):
          lines.insert(i, '</ul>')
          break
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

def parse_image(text):
  return sub(image_token, image_result, text)

def parse_breakline(text):
  return sub(breakline_token, breakline_result, text)

def parse_paragraph(text):
  lines = text.split('\n')

  for i in range(len(lines)):
    line = lines[i]
    lines[i] = sub(paragraph_token, paragraph_result, line)

  return '\n'.join(lines)

def parse_strike(text):
  return sub(strike_token, strike_result, text)

def parse_blockquote(text):
  lines = text.split('\n')

  for i in range(len(lines)):
    line = lines[i]
    lines[i] = sub(blockquote_token, blockquote_result, line)

  return '\n'.join(lines)

def parse_alternate_header(text):
  lines = text.split('\n')
  index_list = []
  for i in range(len(lines)):
    if search(alternate_header_token_level1, lines[i]) is not None:
      lines[i-1] = sub(alternate_header_token_level1,"<h1>" + lines[i-1] + "</h1>" , lines[i])
      index_list.insert(0,i)
  
  for i in range(len(lines)):
    if search(alternate_header_token_level2, lines[i]) is not None:
      lines[i-1] = sub(alternate_header_token_level2,"<h2>" + lines[i-1] + "</h2>" , lines[i])
      index_list.insert(0,i)

  for i in index_list:
    lines.pop(i)

  return '\n'.join(lines)

def parse_table(text):

  lines = text.split('\n')
  i = 0
  
  while i < len(lines):
    if match(r'^\|(.+?\|)+', lines[i]):
      table, table_size = build_table(lines[i:])
      lines[i:i+table_size] = []
      lines.insert(i, table)
    i += 1
  return '\n'.join(lines)

def build_table(lines):
  i = 0  
  table = ["<table>"]
  amount_pipes = len(lines[0].split('|')) - 2

  if lines[1].startswith('|-'):
    elements = lines[0].split('|')[1:-1]
    row = '<tr>'
    for el in elements:
      row += '<th>' + el + '</th>'
    row += '</tr>'
    table.append(row)
    i += 2

  while i < len(lines):
    if not lines[i].startswith('|'):
      table.append('</table>')
      return ''.join(table), i 

    else:       
      elements = lines[i].split('|')[1:-1]
      while len(elements) < amount_pipes:
        elements.append('')
      
      i += 1
      row = '<tr>'
      for j in range(amount_pipes):
        el = elements[j]
        row += '<td>' + el + '</td>'
      row += '</tr>'
      table.append(row)

  table.append('</table>')
  return ''.join(table), i


def parse_text(markdown):
  
  markdown = parse_header(markdown)
  markdown = parse_alternate_header(markdown)
  markdown = parse_blockquote(markdown)
  markdown = parse_unordered_list(markdown)
  markdown = parse_ordered_list(markdown)
  markdown = parse_table(markdown)
  markdown = parse_paragraph(markdown)
  markdown = parse_link(markdown)
  markdown = parse_image(markdown)
  markdown = parse_bold(markdown)
  markdown = parse_italic(markdown)
  markdown = parse_strike(markdown)
  markdown = parse_code(markdown)
  markdown = parse_breakline(markdown)

  return markdown
