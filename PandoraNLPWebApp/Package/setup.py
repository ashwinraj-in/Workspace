from setuptools import find_packages
from setuptools import setup

setup(
  name='PandoraNLP',
  version='1.0.0',
  description='Perform NLP Operations',
  author='Ashwin Raj',
  author_email='rajashwin812@gmail.com',
  url='https://www.python.org/sigs/distutils-sig/',
  packages==find_packages(exclude=('tests*',)),
  license='Apache 2.0',
  keywords='google colab ipython jupyter http_over_ws',
 )