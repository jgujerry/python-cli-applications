# cement-app

## 1. Setup virtual environment

Enter the `cement-app` directory, then create a virtual environment,

```bash
$ python3 -m venv .venv
```

Then activate the virtual environment by running:

```bash
$ source .venv/bin/activate
```

## 2. Install cli app

Install this CLI app in `editable` mode,

```bash
$ pip install -e .
```

When done, it should have `cement-app` package installed with version `0.0.1`.

Validate the installation,

```bash
$ pip show skcli
```

## 3. How to use `skcli`?

Use the commands by following the `--help` instruction,

```bash
$ skcli --help
usage: skcli [-h] [-d] [-q] {add,get,list,remove,update} ...

A simple password management CLI application.

options:
  -h, --help            show this help message and exit
  -d, --debug           full application debug mode
  -q, --quiet           suppress all console output

sub-commands:
  {add,get,list,remove,update}
    add                 add a new password
    get                 get a password
    list                list all passwords
    remove              remove a stored password
    update              update an existing password

Usage: skcli command --appname NAME [--username USERNAME] [--password PASSWORD]

```
