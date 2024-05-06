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
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save_passwords(self):
        with open(PASSWORD_FILE, 'w') as file:
            json.dump(self.data, file, indent=2)

    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()

    def add_password(self, appname, username, password):
        encrypted_password = self.encrypt_password(password)
        self.data[appname] = {'username': username, 'password': encrypted_password}
        self.save_passwords()
        print(f"Password added for {appname}")

    def get_password(self, appname):
        entry = self.data.get(appname)
        if entry:
            print(f"Password for {appname}: {self.decrypt_password(entry['password'])}")
        else:
            print("Password not found")

    def update_password(self, appname, new_password):
        entry = self.data.get(appname)
        if entry:
            new_password = new_password
            encrypted_password = self.encrypt_password(new_password)
            entry['password'] = encrypted_password
            self.save_passwords()
            print(f"Password updated for {appname}")
        else:
            print("Password not found")

    def remove_password(self, appname):
        if appname in self.data:
            del self.data[appname]
            self.save_passwords()
            print(f"Password removed for {appname}")
        else:
            print("Password not found")

    def list_passwords(self):
        for appname, details in self.data.items():
            print(f"Appname: {appname}, Username: {details['username']}")
