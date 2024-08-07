from StarAI.Utils.FilesUtils import *
from pathlib import Path
from typing import final

shift = 54

dict_path: final = Path("Assets/WordDict.json").absolute()


def str_to_int(string):

    string = string.upper()

    num = ""
    for x in range(len(string)):

        r = ord(string[x]) - shift

        num += str(r)

    save_to_json(dict_path, num, string)

    return int(num)


def int_to_str(num):

    num = str(num)

    word = extract_from_json(dict_path, num)
    if word is not None:
        return word

    string = ""

    for i in range(0, len(num), 2):
        sub_num = int(num[i]+num[i+1])
        string += chr(sub_num + shift)

    return string
