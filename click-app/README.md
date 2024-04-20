# click-app

## 1. Setup virtual environment

Enter the `click-app` directory, then create a virtual environment,

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

When done, it should have `click-app` package installed with version `0.0.1`.

Validate the installation,

```bash
$ pip show skcli
```

## 3. `skcli` command usage

Use the commands by following the `--help` instruction,

```bash
$ skcli --help
Usage: skcli [OPTIONS] COMMAND [ARGS]...

  Safekey CLI app built with Click

Options:
  --help  Show this message and exit.

Commands:
  add     Add a new password
  get     Retrieve a password
  remove  Remove a password
  update  Update a password
```
