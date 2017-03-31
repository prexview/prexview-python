# ![PrexView](https://prexview.com/media/extension/promo.png)

[![Status](https://travis-ci.org/prexview/prexview-python.svg?branch=master)](https://travis-ci.org/prexview/prexview-python)

A pip library to use PrexView a fast, scalable and very friendly service for programatic HTML, PDF, PNG or JPG generation using JSON or XML data.

*See [PrexView](https://prexview.com) for more information about the service.*


## Install pip

```
pip install prexview
```

## Usage

###### Set up the PXV_API_KEY as an environment variable

```
export PXV_API_KEY="API_KEY"
```

If you can't setup the environment variable, create the PrexView object like this

```python
pxv = PrexView('your_token_here')
```

You can get an API Key by downloading PrexView Studio from [PrexView](https://prexview.com).

###### Sending XML

```python
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

file = 'test.pdf'

try:
  res = pxv.sendXML(xml, options)

  with open(file, 'wb') as f:
    f.write(res['file'])
    f.close()

  print 'File created:', file
except Exception as e:
  print e
```

###### Sending JSON

You can pass the json param as a valid json string or as a standard object

```python
# coding: utf-8
from prexview import Prexview

pxv = Prexview()
options = {'design': 'custom-invoice', 'output': 'pdf'}

json = '''{
  "languages": [
    {"code": "en", "name": "English"},
    {"code": "es", "name": "Español"},
    {"code": "fr", "name": "Française"}
  ]
}'''

file = 'test.pdf'

try:
  res = pxv.sendJSON(json, options)

  with open(file, 'wb') as f:
    f.write(res['file'])
    f.close()

  print 'File created:', file
except Exception as e:
  print e
```

## API

### sendXML(xml, options)

Send data as a XML string

### sendJSON(json, options)

Send data as a JSON string, it can also be can be a valid JSON string or a dictionary object

#### Options

##### -\-format

###### Type: `string` **Required: Yes**

Data to use for the document creation, must be xml or json.

##### -\-design

###### Type: `string` **Required: Yes**

Design's name to use.

You can use json sintax here to access data and have dynamic design names
```json
{
  "Data": {
    "customer": "123"
  }
}
```
Design name can use any data attribute or text node
```
invoice-customer-{{Data.customer}}
```
We will translate that to the following
```
invoice-customer-123
```

And finally the service will try to find the design **invoice-customer-123** in order to transform the data and generate the document.
  
##### -\-output

###### Type: `string` **Required: Yes**

Document response type from the service, it can be **html**, **pdf**, **png** or **jpg**.

##### -\-design-backup

###### Type: `string`

Design's name to use to be used if the option **design** is not available in the service.

##### -\-note

###### Type: `string`

Custom note that can be used to add any information, it's limit up to 500 chars. This is useful if you want to add metadata such as document, transaction or customer ID.

You can use json syntax to access data and get dynamic notes. 
  
```json
{
  "Data": {
    "customer": "123"
  }
}
```
Notes can use any data attribute or text
```
Document: Invoice
Customer: {{Data.customer}}
```
We will translate that to the following
```
Document: Invoice
Customer: 123
```


## License

MIT © [PrexView](https://prexview.com)
