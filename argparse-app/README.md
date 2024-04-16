# argparse

Build the password management CLI tool by using Python's built-in package: `argparse`.


## Setup a Virtual Environment

Create a virtual environment,

```bash
$ python -m venv .venv
```

The activate this virtual environment,

```bash
$ source .venv/bin/activate
```

Clone this repo and enter in the directory `argparse-app`,

```bash
$ cd argparse-app
```

Install this CLI tool editabily,

```bash
$ pip install -e .
```

This would install the `safekey` package with `sk` command. Check this:

```bash
$ sk --help
usage: sk [-h] {add,get,update,remove,list} ...

SafeKey CLI Tool

options:
  -h, --help            show this help message and exit

subcommands:
  {add,get,update,remove,list}
    add                 Add a new login
    get                 Retrieve a password
    update              Update a password
    remove              Remove a password
    list                List all passwords

```
