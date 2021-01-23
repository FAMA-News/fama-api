from os.path import exists, isfile, dirname, abspath, sep
import json

class Data:
    __DATA_DIR__ = abspath(dirname(__file__)) + sep

    @classmethod
    def __load__(cls, filename: str) -> str:
        filepath = cls.__DATA_DIR__ + filename
        if not exists(filepath):
            raise ValueError(f"File Not Found in Data Directory ({filename})")

        if not isfile(filepath):
            raise ValueError(f"Path is for Folder ({filename})")

        with open(filepath) as fp:
            return fp.read()

    @classmethod
    def load(cls, filename: str):
        partition = filename.rpartition(".")
        extension = partition[2].upper() if len(partition) == 3 else None
        
        if extension == "JSON":
            string = cls.__load__(filename)
            return json.loads(string)

        raise ValueError("Couldn't")