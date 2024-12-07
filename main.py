import argparse
import pathlib

from dotenv import load_dotenv

import config
import crypto

if __name__ == '__main__':
    if not pathlib.Path(config.ENV_FILENAME).exists():
        with open(config.ENV_FILENAME, 'w') as f:
            f.write('# Add necessary environment variables here\n')

    load_dotenv()

    crypto.make_sure_fernet_key_exists()

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-e', '--file-encrypt')
    group.add_argument('-d', '--file-decrypt')

    args = parser.parse_args()

    if args.file_encrypt:
        crypto.encrypt_file(args.file_encrypt)
    elif args.file_decrypt:
        crypto.decrypt_file(args.file_decrypt)
