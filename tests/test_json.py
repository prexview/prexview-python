# coding: utf-8
from prexview import PrexView

pxv = PrexView()
options = {'design': 'custom-invoice', 'output': 'pdf'}

json = {
  'languages': [
    {"code": "en", "name": "English"},
    {"code": "es", "name": "Español"},
    {"code": "fr", "name": "Française"}
  ]
}

file = 'test_json.pdf'

try:
  res = pxv.sendJSON(json, options)

  with open(file, 'wb') as f:
    f.write(res['file'])
    f.close()

  print('File created:', file)
except Exception as e:
  print(e)
