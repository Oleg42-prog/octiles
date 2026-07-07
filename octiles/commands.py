from octiles.core import is_eq_files, dedup_files, diff_folders
from octiles.validations import validate_paths_are_folders, validate_paths_exists, validate_paths_are_files


def eq_command(path_a: str, path_b: str):
    if not validate_paths_exists(path_a, path_b):
        return
    if not validate_paths_are_files(path_a, path_b):
        return
    print(is_eq_files(path_a, path_b))


def dedup_command(path_a: str, path_b: str):
    if not validate_paths_exists(path_a, path_b):
        return
    if not validate_paths_are_files(path_a, path_b):
        return
    print(dedup_files(path_a, path_b))


def diff_command(path_a: str, path_b: str):
    if not validate_paths_exists(path_a, path_b):
        return
    if not validate_paths_are_folders(path_a, path_b):
        return
    print(diff_folders(path_a, path_b))


def help_command():
    print('octiles <command> <arguments>')
    print('Command list:')
    print('\t- eq <file_path_a> <file_path_b>')
    print('\t- dedup <file_path_a> <file_path_b>')
    print('\t- diff <folder_path_a> <folder_path_b>')
    print('\t- help')
