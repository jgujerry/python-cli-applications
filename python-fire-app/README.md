# python-fire-app


## Setup virtual environment

Enter the `python-fire-app` directory, then create a virtual environment,

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

When done, it should have `python-fire-app` package installed with version `0.0.1`.

Validate the installation,

```bash
$ pip show skcli
```

## 3. How to use `skcli`?

Use the commands by following the `--help` instruction,

```bash
$ skcli --help

NAME
    skcli

SYNOPSIS
    skcli COMMAND

COMMANDS
    COMMAND is one of the following:

     add
       Add a new password entry.

     get
       Get the password for an app.

     update
       Update the password for an app.

     delete
       Delete the password for an app.

     list
       List all password entries.

```
