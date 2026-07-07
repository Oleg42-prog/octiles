import os
import sys


def parse_args() -> tuple[str, str]:
    file_path_a = sys.argv[1]
    file_path_b = sys.argv[2]
    return file_path_a, file_path_b


def is_eq_files(path_a: str, path_b: str) -> bool:
    with open(path_a, 'rb') as file_a:
        with open(path_b, 'rb') as file_b:
            return file_a.read() == file_b.read()


def cmd_is_eq_files():
    file_path_a, file_path_b = parse_args()

    if not os.path.exists(file_path_a):
        print(f'Path file_path_a is not exists: {file_path_a}')

    if not os.path.exists(file_path_b):
        print(f'Path file_path_b is not exists: {file_path_b}')

    result = is_eq_files(file_path_a, file_path_b)
    print(result)
