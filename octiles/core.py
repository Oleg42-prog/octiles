import os
from typing import Iterator
from octiles.models import DiffResult


def file_paths_generator(folder_path: str) -> Iterator[str]:
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            yield file_path


def is_eq_files(path_a: str, path_b: str) -> bool:
    with open(path_a, 'rb') as file_a:
        with open(path_b, 'rb') as file_b:
            return file_a.read() == file_b.read()


def dedup_files(path_a: str, path_b: str) -> bool:
    if not is_eq_files(path_a, path_b):
        return False

    os.remove(path_b)

    return not os.path.exists(path_b)


def diff_folders(folder_path_a: str, folder_path_b: str) -> DiffResult:

    result = DiffResult.create_empty()

    dict_a = {os.path.basename(path): path for path in file_paths_generator(folder_path_a)}
    dict_b = {os.path.basename(path): path for path in file_paths_generator(folder_path_b)}

    set_keys_a = set(dict_a.keys())
    set_keys_b = set(dict_b.keys())

    result.new = [dict_b[key] for key in set.difference(set_keys_b, set_keys_a)]
    result.removed = [dict_a[key] for key in set.difference(set_keys_a, set_keys_b)]
    for key in set.intersection(set_keys_a, set_keys_b):
        file_path_a = dict_a[key]
        file_path_b = dict_b[key]
        if is_eq_files(file_path_a, file_path_b):
            result.equals[key] = (file_path_a, file_path_b)
        else:
            result.unequals[key] = (file_path_a, file_path_b)

    return result
