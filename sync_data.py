#!/usr/bin/python3
"""Synchronizes date from databases"""


from models import storage
import json
from typing import Dict
from models.patient import Patient

sync_data_list: Dict = {
                        "Patient": Patient
                        }



def pull(filepath: str, datas: dict, cls) -> None:
    """update database from file"""
    try:
        with open(filepath, "r") as file:
            file_data = json.load(file)
            count: int = 0
            for data in file_data:
                if data not in datas:
                    new_dict = file_data.get(data)
                    new = cls(**new_dict)
                    new.save()
                    count += 1
        if count > 0:
            print(f"{count} datas added to database")
        else:
            print("No data added to database")
        print("<<<...Database Updated...>>>")
    except FileNotFoundError:
        print("No file found")

def push(filepath: str, datas: dict) -> None:
    """updates file from database"""
    new_data: Dict = {}
    try:
        with open(filepath, "r") as fileread:
            file_data = json.load(fileread)
            for data in datas:
                if data not in file_data:
                    new_data.update({data: datas[data]})
    except FileNotFoundError:
        new_data = datas.copy()

    with open(filepath, "w") as file:
        json.dump(new_data, file)
    print("file data updated for pull")


if __name__ == "__main__":
    for data in sync_data_list:
        datas = storage.all(data)
        file_path = f"{data}.json"
        pull(file_path, datas, sync_data_list[data])
        push(file_path, datas)
