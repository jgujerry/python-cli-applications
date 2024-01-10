import argparse

from stock.core import Stock


def main():
    parser = argparse.ArgumentParser(
        prog="argparse-stock",
        description="Stock CLI app built with Python Argparse",
        epilog="Text at the bottom of help"
    )
    
    parser.add_argument("--log", default="info", choices=["debug", "info", "warning", "error", "critical"])
    
    # Info command
    subparsers = parser.add_subparsers(help="Available Commands")
    subparsers.add_parser("hi-info")
    parser.set_defaults(func=None)


if __name__ == "__main__":
    main()
