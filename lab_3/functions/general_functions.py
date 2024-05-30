import json

from typing import Dict


class Functions:

    @staticmethod
    def read_json_file(source_file_path: str) -> Dict[str, str]:
        try:
            with open(source_file_path, "r", encoding="UTF-8") as file:
                return json.loads(file.read())
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')

    @staticmethod
    def write_bytes(key: bytes, source_file_path: str) -> None:
        try:
            with open(source_file_path, 'wb') as key_file:
                key_file.write(key)
        except Exception as error:
            raise Exception(f'There is a trouble: {error}')
