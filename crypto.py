import os

from cryptography.fernet import Fernet

import config


def generate_key():
    return Fernet.generate_key()


def encrypt_file(filepath):
    fernet_key = os.environ[config.FERNET_KEY]

    fernet = Fernet(fernet_key)

    with open(filepath, 'rb') as file:
        original = file.read()

        encrypted = fernet.encrypt(original)

    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_file(filepath):
    fernet_key = os.environ[config.FERNET_KEY]

    fernet = Fernet(fernet_key)

    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filepath, 'wb') as dec_file:
        dec_file.write(decrypted)


def make_sure_fernet_key_exists():
    fernet_key = os.environ.get(config.FERNET_KEY)

    if fernet_key:
        return

    fernet_key = generate_key()
    fernet_key_str = fernet_key.decode('utf-8')

    with open(config.ENV_FILENAME, 'a') as f:
        f.write(f"\n{config.FERNET_KEY}='{fernet_key_str}'")

    os.environ[f'{config.FERNET_KEY}'] = fernet_key_str
