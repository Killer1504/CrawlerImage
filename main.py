from app.crawl import crawl_image
import datetime
import os
from os import listdir
from os.path import isfile, join

import random
import string

MAX_IMAGE_NUMBER = 200


def read_key_word(filename):
    '''
    one line as one keyword
    '''
    key_words = []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line)
                key_words.append(line.replace("\n","").replace("\r",""))
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred while reading file: {e}")
    return key_words

def get_date_time():
    return datetime.datetime.now().__str__()

def run_crawl_image(dir_save_root, key_words):

    if os.path.exists(dir_save_root) == False:
        os.mkdir(dir_save_root)


    for item in key_words:
        path_save = os.path.join(dir_save_root, item)
        if os.path.exists(path_save) == False:
            os.mkdir(path_save)
        crawl_image(item, MAX_IMAGE_NUMBER, path_save)
    pass
def rename_image(root_folder):
    # list folder in root
    subfolders = [ f.path for f in os.scandir(root_dir) if f.is_dir() ]
    for sub in subfolders:
        sub_name = sub.split("\\")[-1]
        print(f"All file in {sub}")
        onlyfiles = [f for f in listdir(sub) if isfile(join(sub, f))]
        for file in onlyfiles:
            
            old_name = os.path.join(sub, file)
            extension = file.split(".")[-1]
            name_file = get_random_string(10)
            new_name = os.path.join(sub, sub_name + "_" + name_file + "." + extension);
            print(f"{old_name} ----------> {new_name}")
            os.rename(old_name, new_name)
    # rename file sub folder as prefix is sub_folder_name
    pass

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


if __name__ == "__main__":
    root_dir = "Images_1"
    key_words = read_key_word("keyword.txt")
    # rename_image(root_dir)
    run_crawl_image(root_dir, key_words)

