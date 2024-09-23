import argparse
import pathlib

from cryptography.fernet import Fernet


def generate_key(name):
    key = Fernet.generate_key()

    with open(name, 'wb') as keyfile:
        keyfile.write(key)


def encrypt_file(filepath, key_filename):
    with open(key_filename, 'rb') as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)

    with open(filepath, 'rb') as file:
        original = file.read()

        encrypted = fernet.encrypt(original)

    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_file(filepath, key_filename):
    with open(key_filename, 'rb') as keyfile:
        key = keyfile.read()

    fernet = Fernet(key)

    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filepath, 'wb') as dec_file:
        dec_file.write(decrypted)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keypath', default='keyfile.key')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-fe', '--file-encrypt')
    group.add_argument('-fd', '--file-decrypt')

    args = parser.parse_args()

    keyfile = pathlib.Path(args.keypath)
    if not keyfile.exists():
        generate_key(args.keypath)

    if args.file_encrypt:
        encrypt_file(args.file_encrypt, args.keypath)
    elif args.file_decrypt:
        decrypt_file(args.file_decrypt, args.keypath)
