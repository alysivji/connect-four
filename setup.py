from setuptools import setup, find_packages

setup(
    name='connect-four',
    version='0.0.1',
    description='Connect Four game to practice OOP skills',
    url='https://github.com/alysivji/connect-four',
    author='Aly Sivji',
    author_email='alysivji@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests', ]),
    install_requires=[''],
    download_url='https://github.com/alysivji/connect-four',
)
