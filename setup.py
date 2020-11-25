import os
from setuptools import setup, find_packages


DESCRIPTION = 'A small, simple date tool library we use for our dashboards.'
HERE_PATH = os.path.dirname(os.path.abspath(__file__))
VERSION = '0.0.1'


try:
    with open(os.path.join(HERE_PATH, 'README.md')) as f:
        long_description = '\n' + f.read()
except IOError:
    long_description = DESCRIPTION


setup(
    name='snekdate',
    version=VERSION,
    author='David Smit',
    author_email='david.d.smit@gmail.com',
    packages=find_packages(),
    license='MIT',
    url='https://github.com/RichFoley/jinjaql',
    description='A small, simple date tool library we use for our dashboards.',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    include_package_data=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)