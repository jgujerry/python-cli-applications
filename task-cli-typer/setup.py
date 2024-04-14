from setuptools import setup, find_packages


setup(
    name='task-cli-typer',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'typer',
    ],
    entry_points={
        'console_scripts': [
            'task=cli.main:main',
        ],
    },
)
