import os
from typing import Callable


def validate_paths(predicate: Callable, path_a: str, path_b: str, error_message: str) -> bool:
    is_valid = True

    if not predicate(path_a):
        is_valid = False
        print(f'Path path_a is {error_message}: {path_a}')

    if not predicate(path_b):
        is_valid = False
        print(f'Path path_b is {error_message}: {path_b}')

    return is_valid


def validate_paths_exists(path_a: str, path_b: str) -> bool:
    return validate_paths(os.path.exists, path_a, path_b, 'not exists')


def validate_paths_are_folders(path_a: str, path_b: str) -> bool:
    return validate_paths(os.path.isdir, path_a, path_b, 'not folder')


def validate_paths_are_files(path_a: str, path_b: str) -> bool:
    return validate_paths(os.path.isfile, path_a, path_b, 'not file')
