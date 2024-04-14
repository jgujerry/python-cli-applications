from setuptools import setup, find_packages


setup(
    name='safekey',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'sk=cli.main:main',
        ],
    },
)
