import os
import sys


def parse_args() -> tuple[bool, str, str]:
    is_args_valid = True
    file_path_a = sys.argv[1]
    file_path_b = sys.argv[2]

    if not os.path.exists(file_path_a):
        is_args_valid = False
        print(f'Path file_path_a is not exists: {file_path_a}')

    if not os.path.exists(file_path_b):
        is_args_valid = False
        print(f'Path file_path_b is not exists: {file_path_b}')

    return is_args_valid, file_path_a, file_path_b


def is_eq_files(path_a: str, path_b: str) -> bool:
    with open(path_a, 'rb') as file_a:
        with open(path_b, 'rb') as file_b:
            return file_a.read() == file_b.read()


def dedup_files(path_a: str, path_b: str) -> bool:
    if not is_eq_files(path_a, path_b):
        return False

    os.remove(path_b)

    return not os.path.exists(path_b)


def cmd_is_eq_files():
    is_args_valid, file_path_a, file_path_b = parse_args()
    if not is_args_valid:
        return

    result = is_eq_files(file_path_a, file_path_b)
    print(result)


def cmd_dedup_files():
    is_args_valid, file_path_a, file_path_b = parse_args()
    if not is_args_valid:
        return

    result = dedup_files(file_path_a, file_path_b)
    print(result)
