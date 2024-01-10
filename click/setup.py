from setuptools import setup, find_packages


setup(
    name='stock',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'yfinance',
    ],
    entry_points={
        'console_scripts': [
            'stock=cli.main:main',
        ],
    },
)
