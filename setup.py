try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import opam

with open("README.md") as readme_file:
    readme_string = readme_file.read()

setup(
    name="opam",
    version="1.0.6",
    description="Python Library for opam",
    author="Rohit Potter",
    author_email="rohitpotter12@gmail.com",
    url="https://github.com/rpotter12/opam",
    packages=['opam'],
    license="MIT",
    long_description=readme_string,
    python_requires=">=2.6",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
