# click-app

## 1. Setup virtual environment

Enter the `cliff-app` directory, then create a virtual environment,

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

When done, it should have `cliff-app` package installed with version `0.0.1`.

Validate the installation,

```bash
$ pip show skcli
```

## 3. How to use `skcli`?

Use the commands by following the `--help` instruction,

```bash
$ skcli --help
usage: skcli [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]

SKCLI Password Manager

options:
  --version             show program's version number and exit
  -v, --verbose         Increase verbosity of output. Can be repeated.
  -q, --quiet           Suppress output except warnings and errors.
  --log-file LOG_FILE
                        Specify a file to log output. Disabled by default.
  -h, --help            Show help message and exit.
  --debug               Show tracebacks on errors.

Commands:
  add  Add a new password
  complete  print bash completion command (cliff)
  get  Get a password
  help  print detailed help for another command (cliff)
  list  List all saved passwords
  remove  Remove a password entry
  update  Update an existing password

```
