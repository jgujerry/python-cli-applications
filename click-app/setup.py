from setuptools import setup, find_packages


setup(
    name='task-cli-click',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'task=cli.main:main',
        ],
    },
)
