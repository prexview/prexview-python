# coding: utf-8
from prexview import Prexview

pxv = Prexview()
options = {'design': 'custom-invoice', 'output': 'pdf'}

json = '''{
  "languages": {
    "en": "English",
    "es": "Español",
    "fr": "Française"
  }
}'''

file = '/tmp/test.pdf'

try:
  res = pxv.sendJSON(json, options)

  with open(file, 'wb') as f:
    f.write(res['file'])
    f.close()

  print 'File created:', file
except Exception as e:
  print e
