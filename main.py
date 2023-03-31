__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    final_directory = os.path.join(current_directory, r"cache")
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    else:
        list_files = os.listdir(final_directory)
        for f in list_files:
            os.remove(os.path.join(final_directory, f))


clean_cache()


def cache_zip(zip_file, cache_dir):
    with ZipFile(zip_file, "r") as zObject:
        zObject.extractall(path=cache_dir)


cache_zip(
    "/Users/valentinamazzucato/Desktop/Sasha/Winc/Python(BackEnd)/files/data.zip",
    "/Users/valentinamazzucato/Desktop/Sasha/Winc/Python(BackEnd)/files/cache",
)


def cached_files():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    final_directory = os.path.join(current_directory, r"cache")
    list_files = os.listdir(final_directory)
    list_paths = []
    for file in list_files:
        if os.path.isfile(os.path.join(final_directory, file)):
            list_paths.append(os.path.join(final_directory, file))
    return list_paths


cached_files()


def find_password(cached_files):
    for x in cached_files:
        with open(x, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.find("password") != -1:
                    return line


find_password(cached_files())
