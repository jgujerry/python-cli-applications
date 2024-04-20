from setuptools import setup, find_packages


setup(
    name='click-app',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'cryptography'
    ],
    entry_points={
        'console_scripts': [
            'sk=cli.main:main',
        ],
    },
)
