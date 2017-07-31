from setuptools import setup

setup(
  name='prexview',

  version='1.1.0',
  description='A Python package to use PrexView a fast, scalable and friendly service for programatic HTML, PDF, PNG or JPG generation using JSON or XML data.',

  # long_description=long_description,

  url='https://github.com/prexview/prexview-python',

  download_url='https://github.com/prexview/prexview-python/archive/1.1.0.tar.gz',

  # Author details
  author='PrexView',
  author_email='code@prexview.com',

  license='MIT',

  classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
  ],

  keywords=[
    'xml',
    'json',
    'converter',
    'convert',
    'transform',
    'image',
    'xml-parser',
    'json-parser',
    'document-conversion',
    'xml-to-pdf',
    'xml-to-png',
    'xml-to-jpg',
    'xml-to-html',
    'json-to-pdf',
    'json-to-png',
    'json-to-jpg',
    'json-to-html',
    'html-to-pdf',
    'html-to-png',
    'html-to-jpg',
    'pdf',
    'html',
    'png',
    'jpg',
    'renderer',
    'prexview'
  ],

  packages=[],

  py_modules=['prexview'],

  install_requires=['requests']
)
