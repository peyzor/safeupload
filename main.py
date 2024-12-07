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
    group.add_argument('-e', '--encrypt-file')
    group.add_argument('-d', '--decrypt-file')

    args = parser.parse_args()

    if args.encrypt_file:
        crypto.encrypt_file(args.encrypt_file)
    elif args.decrypt_file:
        crypto.decrypt_file(args.decrypt_file)
