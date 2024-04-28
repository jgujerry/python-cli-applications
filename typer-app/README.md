# typer-app


## Setup virtual environment

Enter the `typer-app` directory, then create a virtual environment,

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

When done, it should have `typer-app` package installed with version `0.0.1`.

Validate the installation,

```bash
$ pip show skcli
```

## 3. How to use `skcli`?

Use the commands by following the `--help` instruction,

```bash
$ skcli --help
                                                                                                                      
 Usage: skcli [OPTIONS] COMMAND [ARGS]...                                                                             
                                                                                                                      
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                            │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.     │
│ --help                        Show this message and exit.                                                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ add      Add a new password entry.                                                                                 │
│ get      Get a password for an app.                                                                                │
│ list     List all passwords.                                                                                       │
│ remove   Remove a password for an app.                                                                             │
│ update   Update a password for an app.                                                                             │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯



```
