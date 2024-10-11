import argparse
import os
import pathlib

from cryptography.fernet import Fernet
from dotenv import load_dotenv

ENV_FILENAME = '.env'
FERNET_KEY = 'FERNET_KEY'


def generate_key():
    return Fernet.generate_key()


def encrypt_file(filepath):
    fernet_key = os.environ[FERNET_KEY]

    fernet = Fernet(fernet_key)

    with open(filepath, 'rb') as file:
        original = file.read()

        encrypted = fernet.encrypt(original)

    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_file(filepath):
    fernet_key = os.environ[FERNET_KEY]

    fernet = Fernet(fernet_key)

    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filepath, 'wb') as dec_file:
        dec_file.write(decrypted)


def make_sure_fernet_key_exists():
    fernet_key = os.environ.get(FERNET_KEY)

    if fernet_key:
        return

    fernet_key = generate_key()
    fernet_key_str = fernet_key.decode('utf-8')

    with open(ENV_FILENAME, 'a') as f:
        f.write(f"\n{FERNET_KEY}='{fernet_key_str}'")

    os.environ[f'{FERNET_KEY}'] = fernet_key_str


if __name__ == '__main__':
    if not pathlib.Path(ENV_FILENAME).exists():
        with open(ENV_FILENAME, 'w') as f:
            f.write('# Add necessary environment variables here\n')

    load_dotenv()

    make_sure_fernet_key_exists()

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-fe', '--file-encrypt')
    group.add_argument('-fd', '--file-decrypt')

    args = parser.parse_args()

    if args.file_encrypt:
        encrypt_file(args.file_encrypt)
    elif args.file_decrypt:
        decrypt_file(args.file_decrypt)
