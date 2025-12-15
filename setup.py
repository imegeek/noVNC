import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.2.6'
DESCRIPTION = "noVNC is a Python-based server that integrates noVNC and websockify to provide a web-based VNC client, enabling remote desktop access via a web browser."

# Setting up
setup(
    name="novnc",
    version=VERSION,
    author="Ankush Bhagat",
    author_email="<ankushbhagatofficial@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    entry_points={
        'console_scripts': ['novnc = novnc:main'],
    },
    packages=find_packages(),
    install_requires=[" websockify"],
    include_package_data=True,
    keywords=['python', 'novnc', 'vnc', "web"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
