from os import getenv
from json import loads, JSONEncoder
from requests import post

class _Singleton(type):
  """ A metaclass that creates a Singleton base class when called. """
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
    else:
      cls._instances[cls].__init__(*args, **kwargs)
    return cls._instances[cls]

class Singleton(_Singleton('SingletonMeta', (object,), {})): pass

class PrexView(Singleton):

  _URL = 'https://api.prexview.com/v1/'

  def __init__(self, token = getenv('PXV_API_KEY')):
    self.token = token

  def __send(self, data):
    headers = {
      'Authorization': self.token
    }

    response = post(self._URL + 'transform', data = data, headers = headers)

    if response.raise_for_status() is not None:
      return None

    result = {
      'rateLimit': response.headers['x-ratelimit-limit'],
      'rateLimitReset': response.headers['x-ratelimit-reset'],
      'rateRemaining': response.headers['x-ratelimit-remaining'],
    }

    if response.status_code is 200:
      result['id'] = response.headers['x-transaction-id']
      result['file'] = response.content
      result['responseTime'] = response.headers['x-response-time']

    return result

  def __isJson(self, str):
    try:
      json = loads(str)
    except ValueError, e:
      return False

    return True

  def __checkOptions(self, _format, options):
    # JSON
    if _format is 'json':
      if type(options['json']) is str:
        if self.__isJson(options['json']) is not True:
          raise Exception('PrexView content must be a valid JSON string')

      else:
        if options['json'] is None or type(options['json']) is not dict:
          raise Exception('PrexView content must be a dictionary object or a valid JSON string')
        else:
          options['json'] = JSONEncoder().encode(options['json'])

    # XML
    else:
      if type(options['xml']) is not str:
        raise Exception('PrexView content must be a valid XML string')

    # TODO: design option is deprecated, this should be removed
    if 'design' in options:
      print('Prexview property "design" is deprecated, please use "template" property')
      options['template'] = options['design']
      del options['design']

    if type(options['template']) is not str:
      raise Exception('PrexView property "template" must be passed as a string option')

    if type(options['output']) is not str:
      raise Exception('PrexView property "output" must be passed as a string option')

    if options['output'] not in ['html','pdf','png','jpg']:
      raise Exception('PrexView property "output" must be one of these options: html, pdf, png or jpg')

    # TODO: designBackup option is deprecated, this shuold be removed
    if 'designBackup' in options:
      print('Prexview property "designBackup" is deprecated, please use "templateBackup" property')
      options['templateBackup'] = options['designBackup']
      del options['designBackup']

    if 'templateBackup' in options and type(options['templateBackup']) is not str:
      raise Exception('PrexView property "templateBackup" must be a string')

    if 'note' in options:
      if type(options['note']) is not str:
        raise Exception('PrexView property "note" must be a string')

      if len(options['note']) > 500:
        options['note'] = options['note'][0:500]

    return options

  def __checkToken(self):
    if self.token is None or self.token is '':
      raise Exception('PrexView environment variable PXV_API_KEY must be set')

  def sendXML(self, content, options):
    self.__checkToken()

    options['xml'] = content

    result = self.__checkOptions('xml', options)

    return self.__send(result)

  def sendJSON(self, content, options):
    self.__checkToken()

    options['json'] = content

    result = self.__checkOptions('json', options)

    return self.__send(result)
