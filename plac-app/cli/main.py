# cli.py
import sys
import plac
from safekey.app import SafeKey


# @plac.opt('--appname', "Application name")
# @plac.opt('--username', "User name")
# @plac.opt('--password', "Password")
# def add(appname: str, username: str, password: str):
#     sk = SafeKey()
#     print(sk.add_password(appname, username, password))


# @plac.opt('--appname', "Application name")
# def get(appname: str):
#     sk = SafeKey()
#     print(sk.get_password(appname))


# def list_():
#     sk = SafeKey()
#     print(sk.list_passwords())


# @plac.opt('--appname', "Application name")
# @plac.opt('--new-password', "Application name")
# def update(appname: str, new_password: str):
#     sk = SafeKey()
#     print(sk.update_password(appname, new_password))


# @plac.opt('--appname', "Application name")
# def remove(appname: str):
#     sk = SafeKey()
#     print(sk.remove_password(appname))


# def main():
#     if len(sys.argv) > 1:
#         command = sys.argv[1].strip()
#     else:
#         print("Usage: skcli [command]")
#         print("Commands: add, get, list, update, remove")
#         return

#     commands = {
#         'add': add,
#         'get': get,
#         'list': list_,
#         'update': update,
#         'remove': remove
#     }

#     if command in commands:
#         plac.call(commands[command])
#     else:
#         print("Unknown command. Available commands: add, get, list, update, remove")


# if __name__ == '__main__':
#     main()

# import plac

# # Add decorators to the function
# @plac.pos('model', help="model name", choices=['A', 'B', 'C'])
# @plac.opt('iter', help="iterations", type=int)
# @plac.flg('debug', help="debug mode")
# def main(model, iter=100, debug=False):
#     """
#     A script for machine learning
#     """
#     print (model, iter, debug)

# if __name__ == '__main__':
#     # Execute function via plac.call().
#     plac.call(main)


import plac

@plac.pos('model', help="model name", choices=['A', 'B', 'C'])
@plac.opt('iter', help="iterations", type=int)
@plac.flg('debug', help="debug mode")
def demo(model, iter=100, debug=False):
    """
    A script for machine learning
    """
    print (model, iter, debug)


def main():
    # Execute function via plac.call()
    plac.call(demo)


if __name__ == '__main__':
    main()
