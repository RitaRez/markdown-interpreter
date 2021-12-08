import sys

from flask import *
from  src.lexinterpreter import parse_text

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello, World!"

@app.route('/convert/', methods=['POST'])
def convert():

  markdown = request.json['markdown']
  html = parse_text(markdown)

  return html, 201

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4200)