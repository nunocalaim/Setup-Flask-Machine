# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "tracking_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Tracking API",
    author_email="",
    url="",
    keywords=["Swagger", "Tracking API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['tracking_server=tracking_server.__main__:main']},
    long_description="""\
     There is no authentication needed for this server.
    """
)
