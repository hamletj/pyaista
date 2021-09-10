import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

# This call to setup() does all the work
setup(
    name='pyaista',
    packages=['pyaista'],
    version='0.0.1',
    license='Apache-2.0',
    description='AISTA Library',
    author='AISTA',
    author_email='NA@NA',
    url='https://github.com/hamletj/pyaista',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache-2.0 License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)