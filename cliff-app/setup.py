from setuptools import setup, find_packages


setup(
    name='skcli',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cliff',
        'cryptography'
    ],
    entry_points={
        'console_scripts': [
            'skcli=cli.main:main',
        ],
        'skcli.commands': [
            'add = cli.commands.add:Add',
            'get = cli.commands.get:Get',
            'list = cli.commands.list:List',
            'update = cli.commands.update:Update',
            'remove = cli.commands.remove:Remove'
        ],
    },
)
