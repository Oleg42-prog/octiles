from octiles.core import is_eq_files, dedup_files
from octiles.validations import validate_paths_exists


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
