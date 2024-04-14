import argparse

from safekey import SafeKey


def main():
    print("Starting...")
    parser = argparse.ArgumentParser(
        prog="argparse-stock",
        description="Stock CLI app built with Python Argparse",
        epilog="Text at the bottom of help"
    )
    
    parser.add_argument("--log", default="info", choices=["debug", "info", "warning", "error", "critical"])
    
    # Info command
    subparsers = parser.add_subparsers(help="Available Commands")
    info_parser = subparsers.add_parser("hi-info")
    info_parser.add_argument("hello", metavar="Hello")
    # info_parser.set_defaults(func=get_stock_info)


if __name__ == "__main__":
    main()
