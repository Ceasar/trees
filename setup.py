from distutils.core import setup

from trees import __version__

# To install the penncoursereview library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup(
    name="trees",
    version=__version__,
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="https://github.com/Ceasar/trees",
    description="Collection of various tree-like data structures",
    keywords=['tree', 'data'],
    packages=['trees'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        ],
    long_description="""\
    A collection of various tree-like data structures.

    Includes:
    -   AutovivifiedDict
    -   Heap (heapq wrapper)
     """)
