import re
from setuptools import setup

import dotgit

setup(
    name="dotgit",
    version=dotgit.__version__,
    author=re.sub(r'\s+<.*', r'', dotgit.__author__),
    author_email=re.sub(r'(^.*<)|(>.*$)', r'', dotgit.__author__),
    url=dotgit.__url__,
    description='.git directory downloader',
    long_description=open('README.rst').read(),
    license="BSD",
    py_modules=['dotgit'],
    entry_points={
        'console_scripts': [
            'dotgit=dotgit:main'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
)
