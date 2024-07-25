# Python CLI Applications

Exploring Python command-line interface (CLI) packages with example applications.


There are several available packages for building CLI applications in Python.

* [Argparse](https://docs.python.org/3/library/argparse.html)
* [Click](https://click.palletsprojects.com/)
* [Typer](https://github.com/tiangolo/typer)
* [Python Fire](https://github.com/google/python-fire)
* [Prompt Toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)
* [Cement](https://github.com/datafolklabs/cement)
* [Cliff](https://github.com/openstack/cliff)
* [Plac](https://github.com/ialbert/plac)
* [Docopt-ng](https://github.com/jazzband/docopt-ng)

## `skcli` for password management

In this project, we are going to build a CLI app called `skcli` to manage password of different applications. This CLI app will be implemented by using each package listed above.

For concrete implementation using each Python package, please see below:

* [argparse-app](./argparse-app/README.md)
* [click-app](./click-app/README.md)
* [typer-app](./typer-app/README.md)
* [python-fire-app](./python-fire-app/README.md)
* [prompt-toolkit-app](./prompt-toolkit-app/README.md)
* [cement-app](./cement-app/README.md)
* [cliff-app](./cliff-app/README.md)
* [plac-app](./plac-app/README.md)
* [docopt-ng-app](./docopt-ng-app/README.md)

To try each example CLI app, the steps are:

* enter into the directory
* create a Python virtual environment by run `python -m venv .venv`
* run `pip install -e .`
* test `skcli --help` to explore the usage.


## Contact

If you have any question about this opinionated list, do not hesitate to contact me [@jgujerry](https://twitter.com/jgujerry) on X (Twitter) or open an issue on GitHub.


## License

This project is released under [MIT License](LICENSE)
