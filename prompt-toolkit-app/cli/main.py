from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

from safekey.app import SafeKey


def main():
    session = PromptSession()
    skcli_completer = WordCompleter([
        'add', 'get', 'list', 'update', 'remove'
    ], ignore_case=True)

    manager = SafeKey()

    while True:
        try:
            text = session.prompt('skcli> ', completer=skcli_completer)
            parts = text.strip().split()
            command = parts[0] if parts else None

            if command == 'add' and len(parts) == 4:
                _, appname, username, password = parts
                manager.add_password(appname, username, password)

            elif command == 'get' and len(parts) == 2:
                _, appname = parts
                manager.get_password(appname)

            elif command == 'list' and len(parts) == 1:
                manager.list_passwords()

            elif command == 'update' and len(parts) == 3:
                _, appname, password = parts
                manager.update_password(appname, password)

            elif command == 'remove' and len(parts) == 2:
                _, appname = parts
                manager.remove_password(appname)

            else:
                print("Unknown command or incorrect usage")

        except KeyboardInterrupt:
            break
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

    print("Goodbye!")

if __name__ == '__main__':
    main()
