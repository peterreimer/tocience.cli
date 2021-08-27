#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = "0.1"


def _read(doc):
    return open(doc, 'rb').read()


setup(
    name="toscience.cli",
    version=__version__,
    author="Peter Reimer",
    author_email="reimer@hbz-nrw.de",
    description="Command line interface to the various to.science rest apis.",
    long_description=_read('README.rst').decode('utf-8'),
    install_requires=[
        'setuptools',
        'argparse',
        'requests',
        'bitmath'

    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
    ],
    license="DFSL",
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['toscience', 'toscience.cli'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'toscience=toscience.cli.cli:main',
            'sizes=toscience.cli.sizes:main',
        ]
    },
)
