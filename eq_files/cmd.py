import os
import sys


def parse_args() -> tuple[bool, str, str]:
    is_args_valid = True
    path_a = sys.argv[1]
    path_b = sys.argv[2]

    if not os.path.exists(path_a):
        is_args_valid = False
        print(f'Path path_a is not exists: {path_a}')

    if not os.path.exists(path_b):
        is_args_valid = False
        print(f'Path path_b is not exists: {path_b}')

    return is_args_valid, path_a, path_b


def parse_args_files() -> tuple[bool, str, str]:
    is_args_valid, path_a, path_b = parse_args()

    if not os.path.isfile(path_a):
        is_args_valid = False
        print(f'Path path_a is not file: {path_a}')

    if not os.path.isfile(path_b):
        is_args_valid = False
        print(f'Path path_b is not file: {path_b}')

    return is_args_valid, path_a, path_b


def parse_args_folders() -> tuple[bool, str, str]:
    is_args_valid, path_a, path_b = parse_args()

    if not os.path.isdir(path_a):
        is_args_valid = False
        print(f'Path path_a is not dir: {path_a}')

    if not os.path.isdir(path_b):
        is_args_valid = False
        print(f'Path path_b is not dir: {path_b}')

    return is_args_valid, path_a, path_b


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
    print(is_eq_files(file_path_a, file_path_b))


def cmd_dedup_files():
    is_args_valid, file_path_a, file_path_b = parse_args()
    if not is_args_valid:
        return
    print(dedup_files(file_path_a, file_path_b))


def cmd_dedup_folders():
    is_args_valid, file_path_a, file_path_b = parse_args()
    if not is_args_valid:
        return
    print(dedup_files(file_path_a, file_path_b))
