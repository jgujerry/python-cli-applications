import argparse
import json
import hashlib
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)


class SafeKey:
    def __init__(self):
        # Generate a key for encryption
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        # Load password entries from file
        try:
            with open('passwords.json', 'r') as file:
                self.passwords = json.load(file)
        except FileNotFoundError:
            self.passwords = {}

    def save_passwords(self):
        with open('passwords.json', 'w') as file:
            json.dump(self.passwords, file)

    def encrypt_password(self, password):
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher.decrypt(encrypted_password.encode()).decode()

    def add_password(self, args):
        website = args.website
        username = args.username
        password = args.password
        encrypted_password = self.encrypt_password(password)
        self.passwords[website] = {'username': username, 'password': encrypted_password}
        self.save_passwords()
        print(f"Password added for {website}")

    def get_password(self, args):
        website_or_username = args.website_or_username
        entry = self.passwords.get(website_or_username)
        if entry:
            print(f"Password for {website_or_username}: {self.decrypt_password(entry['password'])}")
        else:
            print("Password not found")

    def update_password(self, args):
        website_or_username = args.website_or_username
        entry = self.passwords.get(website_or_username)
        if entry:
            new_password = args.new_password
            encrypted_password = self.encrypt_password(new_password)
            entry['password'] = encrypted_password
            self.save_passwords()
            print(f"Password updated for {website_or_username}")
        else:
            print("Password not found")

    def remove_password(self, args):
        website_or_username = args.website_or_username
        if website_or_username in self.passwords:
            del self.passwords[website_or_username]
            self.save_passwords()
            print(f"Password removed for {website_or_username}")
        else:
            print("Password not found")

    def list_passwords(self, args):
        for website, details in self.passwords.items():
            print(f"Website/App: {website}, Username: {details['username']}")