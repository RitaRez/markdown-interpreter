import sys
from tkhtmlview import HTMLLabel
try:
  import Tkinter as tk # for Python2
except ImportError:
  import tkinter as tk # for Python3

from  src.lexinterpreter import parse_text

def setup_window(name):
  window = tk.Tk()
  window.configure(background='white')
  window.title(name)
  return window

def display_html(html, file_path):
  root = setup_window(file_path.split('/')[-1])
  my_label = HTMLLabel(root, html=html)
  my_label.pack(fill='both', expand=True)
  root.mainloop()

def main():
  with open(sys.argv[1]) as f:
    markdown = f.read()
    html = parse_text(markdown)
    # print(html)
    display_html(html, sys.argv[1])

if __name__=='__main__':
  main()