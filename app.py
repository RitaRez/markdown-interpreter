import sys

from flask import *
from flask_cors import CORS, cross_origin


sys.path.insert(1, './api')
from  src.lexinterpreter import parse_text

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
  return "Hello, World!!!"

@app.route('/convert/', methods=['POST'])
@cross_origin()
def convert():

  markdown = request.json['markdown']
  html = parse_text(markdown)

  return html, 201

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4200)