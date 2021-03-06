import sys
from tkhtmlview import HTMLLabel
try:
  import Tkinter as tk # for Python2
except ImportError:
  import tkinter as tk # for Python3

from  src.lexinterpreter import parse_text

def setup_window(name):
  window = tk.Tk()
  window.geometry("900x"+str(window.winfo_screenheight()))
  window.configure(background='white')
  window.title(name)
  return window

def save_html(html, output_file):
  with open(output_file, 'w') as output:
    output.write(html)
    output.close()

def display_html(html, file_path):
  root = setup_window(file_path.split('/')[-1])
  my_label = HTMLLabel(root, html=html)
  my_label.pack(fill='both', expand=True)
  root.mainloop()

def main():
  if len(sys.argv) < 2:
    print("Too few arguments")
    return 

  with open(sys.argv[1]) as input:
    with open("template.html") as template_file:
      template = template_file.read()
      markdown = input.read()
      input.close()
      html = template.replace('{{content}}', parse_text(markdown)).replace('{{title}}', sys.argv[1].split('/')[-1])

      if len(sys.argv) > 2:
        save_html(html, sys.argv[2])
      else:
        display_html(html, sys.argv[1])

if __name__=='__main__':
  main()