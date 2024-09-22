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
    key_filename = 'keyfile.key'
    filepath = '/Users/peyman627/Downloads/nba.csv'
    generate_key(key_filename)
    encrypt_file(filepath, key_filename)
    decrypt_file(filepath, key_filename)
