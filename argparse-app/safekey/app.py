import configparser
import json
from pathlib import Path
from cryptography.fernet import Fernet

CONFIG_DIR = Path.home() / '.skcli'
CONFIG_DIR.mkdir(exist_ok=True)

CONFIG_FILE = CONFIG_DIR / '.config.ini'
PASSWORD_FILE = CONFIG_DIR / 'passwords.json'


def get_secret_key():
    """
    Warning: This is not a secure way to store the key. 
    It is just for demonstration purposes.
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    key = config.get("settings", "key", fallback=None)
    
    if key is None:
        key = Fernet.generate_key()
        config["settings"] = {"key": key.decode()}
        with open(CONFIG_FILE, "w") as configfile:
            config.write(configfile)
    
    return key



class SafeKey:
    def __init__(self):
        # Generate a key for encryption
        self.key = get_secret_key()
        self.cipher = Fernet(self.key)
        # Load password entries from file
        try:
            with open(PASSWORD_FILE, 'r') as file:
                self.safekeys = json.load(file)
        except FileNotFoundError:
            self.safekeys = {}

    def save_passwords(self):
        with open(PASSWORD_FILE, 'w') as file:
            json.dump(self.safekeys, file)

    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()

    def add_password(self, args):
        appname = args.appname
        username = args.username
        password = args.password
        encrypted_password = self.encrypt_password(password)
        self.safekeys[appname] = {'username': username, 'password': encrypted_password}
        self.save_passwords()
        print(f"Password added for {appname}")

    def get_password(self, args):
        appname = args.appname
        entry = self.safekeys.get(appname)
        if entry:
            print(f"Password for {appname}: {self.decrypt_password(entry['password'])}")
        else:
            print("Password not found")

    def update_password(self, args):
        appname = args.appname
        entry = self.safekeys.get(appname)
        if entry:
            new_password = args.new_password
            encrypted_password = self.encrypt_password(new_password)
            entry['password'] = encrypted_password
            self.save_passwords()
            print(f"Password updated for {appname}")
        else:
            print("Password not found")

    def remove_password(self, args):
        appname = args.appname
        if appname in self.safekeys:
            del self.safekeys[appname]
            self.save_passwords()
            print(f"Password removed for {appname}")
        else:
            print("Password not found")

    def list_passwords(self, args):
        for appname, details in self.safekeys.items():
            print(f"Appname: {appname}, Username: {details['username']}")
