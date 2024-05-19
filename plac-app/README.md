# plac-app

## 1. Setup virtual environment

Enter the `plac-app` directory, then create a virtual environment,

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

When done, it should have `plac-app` package installed with version `0.0.1`.

Validate the installation,

```bash
$ pip show skcli
```

## 3. How to use `skcli`?

Use the commands by following the `--help` instruction,

```bash
$ skcli -h
usage: skcli [-h] [-configfile CONFIGFILE]

A minimal interface over a shelve object.

options:
  -h, --help            show this help message and exit
  -configfile CONFIGFILE
                        path name of the shelve
```


Enter into the CLI session, then use the command, or get the help,

```bash
$ skcli
A minimal interface over a shelve object.
Operating on conf.shelve.
Use help to see the available commands.

i> help

special commands
================
.last_tb

custom commands
===============
add  get  help  list  remove  update


i> add -h
usage: skcli add [-h] appname username password

Add new password

positional arguments:
  appname
  username
  password

options:
  -h, --help  show this help message and exit

i> 

```