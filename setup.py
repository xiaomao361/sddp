#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="sddp",
    version='0.1.7',
    author='zhouwei',
    author_email='xiaomao361@163.com',
    url='https://github.com/xiaomao361/sddp',
    description='ding talk sentry plugin',
    license='MIT',
    keywords='sentry dingtalk',
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'sentry>=9.0.0',
        'requests',
    ],
    entry_points={
        'sentry.plugins': [
            'sddp = sddp.plugin:DingTalkPlugin'
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
