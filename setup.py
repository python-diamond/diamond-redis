#!/usr/bin/env python
from setuptools import setup


install_requires = [
    'diamond',
    'redis',
]

setup(
    name='diamond-redis',
    version='0.0.1',
    author='Matt Robenolt',
    author_email='matt@ydekproductons.com',
    url='https://github.com/python-diamond/diamond-redis',
    description='',
    long_description='',
    license='MIT License',
    py_modules=['diamond_redis'],
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'diamond.collectors': [
            'redis = diamond_redis',
        ],
    },
    classifiers=[
        'DO NOT UPLOAD',
    ],
)
