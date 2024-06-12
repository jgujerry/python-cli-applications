# docopt-ng-app

## 1. Setup virtual environment

Enter the `docopt-ng-app` directory, then create a virtual environment,

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

When done, it should have `docopt-ng-app` package installed with version `0.0.1`.

Validate the installation,

```bash
$ pip show skcli
```

## 3. How to use `skcli`?

Use the commands by following the `--help` instruction,

```bash
$ skcli --help
skcli - A simple CLI password manager.

Usage:
  skcli add <appname> <username> <password>
  skcli get <appname>
  skcli list
  skcli update <appname> <new_password>
  skcli remove <appname>
  skcli (-h | --help)
  skcli (-v | --version)

Options:
  -h --help     Show this screen.
  -v --version  Show the version.
Commands:
  add       Add a new password entry.
  get       Retrieve a password entry.
  list      List all password entries.
  update    Update an existing password entry.
  remove    Remove a password entry.
```
