from os import path
from distutils.core import setup

ROOT = path.dirname(__file__)
README = path.join(ROOT, 'README.md')

setup(
    name='xact',
    py_modules = ['xact'],
    url='https://github.com/xof/xact/',
    author='Christophe Pettus',
    author_email='xof@thebuild.com',
    version='1.0',
    license='New BSD license',
    long_description=open(README).read(),
)
