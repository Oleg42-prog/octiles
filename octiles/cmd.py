import os
import sys
from octiles.validations import validate_paths_exists


def is_eq_files(path_a: str, path_b: str) -> bool:
    with open(path_a, 'rb') as file_a:
        with open(path_b, 'rb') as file_b:
            return file_a.read() == file_b.read()


def dedup_files(path_a: str, path_b: str) -> bool:
    if not is_eq_files(path_a, path_b):
        return False

    os.remove(path_b)

    return not os.path.exists(path_b)


def eq_command(path_a: str, path_b: str):
    if not validate_paths_exists(path_a, path_b):
        return
    print(is_eq_files(path_a, path_b))


def dedup_command(path_a: str, path_b: str):
    if not validate_paths_exists(path_a, path_b):
        return
    print(dedup_files(path_a, path_b))


def help_command():
    print('octiles <command> <arguments>')
    print('Command list:')
    print('\t- eq <file_path_a> <file_path_b>')
    print('\t- dedup <file_path_a> <file_path_b>')
    print('\t- help')


def cmd():
    if len(sys.argv) < 2:
        help_command()
        return

    command = sys.argv[1]
    arguments = sys.argv[2:]
    match command:
        case 'dedup': dedup_command(*arguments)
        case 'eq': eq_command(*arguments)
        case _: help_command()
