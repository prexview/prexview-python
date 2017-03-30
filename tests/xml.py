# coding: utf-8
from prexview import Prexview

pxv = Prexview()
options = dict(design='custom-invoice', output='pdf')

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<languages>
  <lang code="en">English</lang>
  <lang code="es">Español</lang>
  <lang code="fr">Française</lang>
</languages>'''

file = '/tmp/test.pdf'

try:
  res = pxv.sendXML(xml, options)

  with open(file, 'wb') as f:
    f.write(res['file'])
    f.close()

  print 'File created:', file
except Exception as e:
  print e