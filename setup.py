from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='zojax.feedback',
      version=version,
      description="Simple feedback form for zojax.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Andrey Fedoseev',
      author_email='andrey.fedoseev@gmail.com',
      url='',
      license='',
      packages=find_packages('src'),
      package_dir={'':'src'},
      namespace_packages=['zojax', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',
            'ZODB3',
            'zope.schema',
            'zope.location',
            'zope.component',
            'zope.interface',
            'zope.event',
            'zope.security',
            'zope.publisher',
            'zope.i18n',
            'zope.i18nmessageid',
            'zope.contentprovider',
            'zope.cachedescriptors',
            'zope.app.container',
            'z3c.schema',
            'z3c.form',
            
            'zojax.product',
            'zojax.layoutform',
            'zojax.statusmessage',
            'zojax.mail',
            'zojax.mailtemplate',
            'zojax.controlpanel',
          # -*- Extra requirements: -*-
      ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.app.zcmlfiles',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zope.securitypolicy',
                                  'zojax.autoinclude',
                                  'zojax.content.space',
                                  ]),
      entry_points="""
      # -*- Entry points: -*-
      """,
      dependency_links = ['http://download.zope.org/distribution', 'http://eggs.carduner.net/'],
      )
