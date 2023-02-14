import sys
import requests
import hashlib
import os


def download_file(url: str, filename: str, timeout: int = 10):
    try:
        print(f'downloading {filename} from {url}...')
        response = requests.get(url, stream=True, timeout=timeout)
        if response.status_code != 200:
            sys.exit(f'Error: Could not connect to server {url} with status code {response.status_code}')
        with open(filename, 'wb') as f:
            total_length = int(response.headers.get('content-length'))
            dl = 0
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(50 * dl / total_length)
                    bar = '\r[%s%s]' % ('=' * done, ' ' * (50 - done))
                    missing_mb = f' {dl / 1024 / 1024:.2f}MB / {total_length / 1024 / 1024:.2f}MB'
                    sys.stdout.write(bar + missing_mb)
                    sys.stdout.flush()
        print(f'\ndownloaded {filename} from {url}...')
    except requests.exceptions.Timeout:
        sys.exit(f'Error: Timeout while connecting to server {url}')


def replace_if_more_recent(file1: str, file2: str):
    if is_file_newer(file1, file2):
        os.remove(file2)
        os.rename(file1, file2)
    else:
        os.remove(file1)


def is_file_newer(file1: str, file2: str) -> bool:
    return get_hash(file1) != get_hash(file2)


def get_hash(file: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
